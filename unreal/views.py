from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


class ArticleList(APIView):
    def get(self, request):
        article_type = request.query_params['articleType']
        if article_type == 'latest':
            article_list = Article.objects.all()
        elif article_type == 'recommend':
            article_list = Article.objects.filter(recommend=True)
        else:
            article_list = Article.objects.filter(article_type=article_type)

        page = request.query_params['currentPage']
        paginator = Paginator(article_list, 15)
        res = paginator.page(page)
        return Response({
            'list': ArticleSerializer(res, many=True).data,
            'count': paginator.num_pages
        })


class ArticleDetail(APIView):
    def get(self, request):
        id_ = request.query_params['article_id']
        article = Article.objects.get(pk=id_)

        return Response({
            'detail': {
                'id': article.id,
                'content': article.content,
                'title': article.title
            }
        })


class CardList(APIView):
    def get(self, request):
        article_type = request.query_params['articleType']
        if article_type == 'latest':
            article_list = Article.objects.all()[0:8]
        elif article_type == 'recommend':
            article_list = Article.objects.filter(recommend=True)[0:8]
        else:
            article_list = Article.objects.filter(article_type=article_type)[0:8]

        return Response({
            'list': ArticleSerializer(article_list, many=True).data
        })


class ArticleComment(APIView):
    def get(self, request):
        article_id = request.query_params['article_id']
        comment_list = Comment.objects.filter(article_id=article_id)
        return Response({
            'list': CommentSerializer(comment_list, many=True).data
        })

    def post(self, request):
        article_id = request.data['article_id']
        content = request.data['content']

        try:
            content_id = Comment.objects.filter(article_id=article_id)[0].content_id + 1
        except IndexError:
            content_id = 1
        Comment.objects.create(article_id=article_id, content=content, content_id=content_id)
        return Response({

        })


class ArticleSecComment(APIView):
    def get(self, request):
        first_comment_id = request.query_params['first_comment_id']
        second_comment_list = SecComment.objects.filter(first_comment_id=first_comment_id)
        return Response({
            'list': SecCommentSerializer(second_comment_list, many=True).data
        })

    def post(self, request):
        first_comment_id = request.data['first_comment_id']
        content = request.data['content']
        try:
            content_id = SecComment.objects.filter(first_comment_id=first_comment_id)[0].content_id + 1
        except IndexError:
            content_id = 1
        SecComment.objects.create(first_comment_id=first_comment_id, content=content, content_id=content_id)
        return Response({})
