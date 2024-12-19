from tweetapp.views import *
from django.urls import path

urlpatterns = [
    path("index/",index,name="index"),
    path("",tweet_list,name="tweet_list"),
    path("create/",tweet_create,name="tweet_create"),
    path("edit/<int:tweet_id>/",tweet_edit,name="tweet_edit"),
    path("delete/<int:tweet_id>/",tweet_delete,name="tweet_delete"),
    path("register/",register,name="register"),

]
