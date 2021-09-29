from django.urls.conf import path
from . import views

app_name='posts'

urlpatterns = [
    path('exchangePost/', views.exchangePostHome, name='exchangePostHome'),
    path('search/', views.search, name='search'),
    path('exchangePost/add-exchange-post/',views.addExchangePost,name='addExchangePost'),
    path('exchangePost/my-exchange-posts/',views.myExPostList,name='myExPostList'),
    path("exchangePost/expid<int:id>",views.exchangePostView,name="exchangePostView"),
    path("exchangePost/delexpid<int:id>",views.delExPost,name="delExPost"),
    path("exchangePost/editexpid<int:id>",views.editExPost,name="editExPost"),
    path("exchangePost/expid<int:id>/offerlist",views.offerlist,name="offerList"),
    path("exchangePost/expid<int:id>/offerlist<int:offeredid>",views.sendOffer,name="sendOffer"),
    path("exchangePost/expid<int:id>/checkofferlist",views.checkOfferList,name="checkOfferList"),
    path("exchangePost/expid<int:id>/checkofferlist<int:offeredid>",views.acceptoffer,name="acceptOffer"),
]