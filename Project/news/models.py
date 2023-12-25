from django.db import models
from django.urls import reverse


class News(models.Model):
    news = 'NW'
    article = 'AR'

    Type = [
        (news, 'новость'),
        (article, 'статья')
    ]

    name = models.CharField(max_length=155)
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
        null=True,
        blank=False,
    )
    release_date = models.DateTimeField(auto_now_add=True)
    article_news = models.CharField(max_length=2, choices=Type, default=news)

    def __str__(self):
        return f'{self.name}, {self.description[:64]}, {self.release_date}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category_name}'



