from django.db import models
from mdeditor.fields import MDTextField


class Article(models.Model):
    class Meta:
        ordering = ['-date']
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = MDTextField()
    article_type = models.IntegerField(choices=(
        (0, '机器学习'),
        (1, '深度学习')
    ))
    recommend = models.BooleanField(db_column='是否推荐', default=True, choices=(
        (True, '是'),
        (False, '否')
    ))

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ['-content_id', 'id']
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)  # 评论
    content_id = models.IntegerField()  # 该article的第几个评论
    date = models.DateTimeField(auto_now_add=True)


class SecComment(models.Model):
    class Meta:
        ordering = ['-content_id', 'id']
    first_comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=1000)  # 评论
    content_id = models.IntegerField()  # 该article的第几个评论
    date = models.DateTimeField(auto_now_add=True)