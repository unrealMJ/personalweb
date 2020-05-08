from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ArticleList.as_view()),
    path('detail/', ArticleDetail.as_view()),
    path('card/list/', CardList.as_view()),
    path('article/comment/', ArticleComment.as_view()),
    path('article/seccomment/', ArticleSecComment.as_view())
]