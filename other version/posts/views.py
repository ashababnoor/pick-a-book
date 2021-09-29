from django.shortcuts import render,redirect
from posts.models import ExchangePost,ExchangePostImage,Offers,ExchangePostDeliveryInfo
from posts.forms import ExchangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def addExchangePost(request):
    print('in addExchangePost')
    if(request.method=='POST'):
        user = request.user
        images = request.FILES.getlist('images')
        print(request.FILES)
        print(images)
        title = request.POST.get('title')
        author= request.POST.get('author')
        purchase= request.POST.get('purchase_date')
        des= request.POST.get('description')
        edi=0
        publisher=''
        if request.POST.get('edition')!='':
            edi=request.POST.get('edition')
        if request.POST.get('publisher')!='':
            publisher = str(request.POST.get('publisher'))
        prefbooks=request.POST.get('prefered_books')
        cat=request.POST.get('catagory')
        print(purchase)

        exchangepost_obj = ExchangePost.objects.create(
            user=user,title=title,author=author,purchase_date=purchase,description=des,edition=edi,publisher=publisher,prefered_books=prefbooks,catagory=cat,
        )
        for img in images:
            img_obj=ExchangePostImage.objects.create(post=exchangepost_obj,image=img)
            print(img_obj)
        return redirect('posts:exchangePostHome')

    return render(request,'posts/addExchangePost.html')


def exchangePostHome(request):
    print('in exchangePostHome')
    data=[]
    expost=ExchangePost.objects.filter(setVisible=1).order_by('-id')
    for i in expost:
        print((i, ExchangePostImage.objects.filter(post=i.id)[0]))
        data.append((i,ExchangePostImage.objects.filter(post=i.id)[0]))
    context = {
        'exposts' : data,
    }
    return render(request,'posts/ExchagePostHome.html',context)

def exchangePostView(request,id):
    print('in exchangePostView')
    temp = ExchangePost.objects.filter(id=id,setVisible=1)
    # temp = temp.object.all()
    img = ExchangePostImage.objects.filter(post=id)
    # img =img.object.all()
    print(f'{len(img)}')
    print(f'{type(temp)}')
    return render(request, 'posts/exchangePostView.html', context={"expost": temp,'images':img})

def offerlist(request,id):
    print('in offerList')
    expost=ExchangePost.objects.filter(user=request.user.id,setVisible=1)
    context={
        'expost':expost,
        'id':id,
    }
    return render(request,'posts/offerList.html',context)

def sendOffer(request,id,offeredid):
    print('in sendOffer')
    if (request.method == 'POST'):
        offered = ExchangePost.objects.filter(id=offeredid)[0]
        offeringFor = ExchangePost.objects.filter(id=id)[0]
        offeredUser = offered.user
        offeringForUser = offeringFor.user
        offeredUserAddr = request.POST.get('address')
        offer=Offers.objects.create(
            offered=offered,offeringFor=offeringFor,offeredUser=offeredUser,offeringForUser=offeringForUser,offeredUserAddr=offeredUserAddr
        )
        return HttpResponse(f'<h1>Offer Sent to {offeringFor.__str__()}. You offered {offered.__str__()}</h1>')
    offer={
        'id1':id,'offeredid1':offeredid
    }
    return render(request, 'posts/getAddressOfferer.html', context={'offer':offer})


def checkOfferList(request,id):
    print('in checkOfferList')
    offeringfor=ExchangePost.objects.filter(id=id,setVisible=1)
    # offers=Offers.objects.filter(offeringFor=offeringfor)
    offers=Offers.objects.filter(offeringFor=id)
    print(offers)
    context={
        'offers':offers,
        'id':id
    }
    return render(request,'posts/checkOfferlist.html',context)

def acceptoffer(request,id,offeredid):
    print('in accpetoffer')
    if (request.method == 'POST'):
        offeringFor = ExchangePost.objects.get(id=id)
        offered = ExchangePost.objects.get(id=offeredid)
        print(f'{offeredid}|{id}')
        offer=Offers.objects.get(offered=offeredid,offeringFor=id)

        addr1=request.POST.get('address')
        addr2=offer.offeredUserAddr
        offeringFor.setVisible=0
        offered.setVisible=0
        offeringFor.save()
        offered.save()
        delivery=ExchangePostDeliveryInfo.objects.create(
            book1=offered,book2=offeringFor,book1DeliveryAddress=addr1,book2DeliveryAddress=addr2,
        )
        # delivery = ExchangePostDeliveryInfo.objects.create(
        #     book1title =offered.title,book1author =offered.author,book1DeliveryAddress=addr1,book2title=offeringFor.title,book2author =offeringFor.author,book2DeliveryAddress=addr2,
        # )
        # offered.delete()
        # offeringFor.delete()
        return HttpResponse(f'<h1>Offer accepted for {offered.__str__()}. You exchanged {offeringFor.__str__()}</h1>')

    offer = {
        'id1': id, 'offeredid1': offeredid
    }
    return render(request, 'posts/getAddressOffered.html', context={'offer': offer})

def myExPostList(request):
    print('in allExPostList')
    uid=request.user.id
    expost=ExchangePost.objects.filter(user=uid,setVisible=1)
    context={
        'expost': expost,
    }
    return render(request,'posts/myExPostList.html',context)

def delExPost(request,id):
    print('in delExPost')
    expost=ExchangePost.objects.get(id=id)
    if expost.user.id == request.user.id:
        expost.setVisible=0
        expost.save()
    return redirect('posts:exchangePostHome')

def editExPost(request,id):
    print('in editExPost')
    expost=ExchangePost.objects.get(id=id)
    if expost.user.id==request.user.id:
        if (request.method == 'POST'):
            user = request.user
            print(request.FILES)
            title = request.POST.get('title')
            author = request.POST.get('author')
            purchase = request.POST.get('purchase_date')
            des = request.POST.get('description')
            edi = 0
            publisher = ''
            if request.POST.get('edition') != '':
                edi = request.POST.get('edition')
            if request.POST.get('publisher') != '':
                publisher = str(request.POST.get('publisher'))
            prefbooks = request.POST.get('prefered_books')

            expost.user=user
            expost.title=title
            expost.author=author
            expost.purchase_date=purchase
            expost.description=des
            expost.edition=edi
            expost.publisher=publisher
            expost.prefered_books=prefbooks

            expost.save()

            # exchangepost_obj = ExchangePost.objects.create(
            #     user=user, title=title, author=author, purchase_date=purchase, description=des, edition=edi,
            #     publisher=publisher, prefered_books=prefbooks,
            # )
            return redirect('posts:exchangePostHome')

        context={
            'expost':expost
        }
        return render(request, 'posts/editExchangePost.html',context)
    return redirect('posts:exchangePostHome')

def search(request):
    print("in search")
    if (request.method == 'POST'):

        return redirect('posts:exchangePostHome')

    excat=ExchangePost.objects.order_by('catagory').distinct()
    return render(request, 'posts/Search.html',context={'excatagory': excat})