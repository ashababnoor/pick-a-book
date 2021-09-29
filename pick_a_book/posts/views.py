from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import PostImage, SellPost
from django.template import context, loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])

#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
    
#     # return HttpResponse("You're looking at question %s." % question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)

#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form

#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_sell_posts'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return SellPost.objects.all().reverse()[:15]


class DetailView(generic.DetailView):
    model = SellPost
    template_name = 'posts/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return SellPost.objects.all()

def addSellPost(request):
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
        price=request.POST.get('price')
        print(purchase)

        sellpost_obj = SellPost.objects.create(
            user=user,title=title,author=author,purchase_date=purchase,description=des,edition=edi,publisher=publisher,price=price,
        )
        for img in images:
            img_obj=PostImage.objects.create(post=sellpost_obj,image=img)
            print(img_obj)
        return redirect('/')

    return render(request,'posts/addSellPost.html')




# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

