from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Tag(models.Model):
    """Модель тэга."""

    title = models.CharField(
        max_length=100,
        verbose_name='Название тэга',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовать'
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self):
        return f'{self.title} - {self.is_published}'


class Post(models.Model):
    """Модель поста."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название поста'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Слаг'
    )
    img = models.ImageField(
        upload_to='blog/posts/',
        verbose_name='Титульная картинка'
    )
    content = HTMLField(
        default='Пишите статью здесь.'
    )
    tag = models.ForeignKey(
        Tag, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='posts',
        verbose_name='Тэг'
    )
    author = models.CharField(
        default='Надежда',
        verbose_name='Автор'
    )
    date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата и время публикации'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return f'{self.title} - {self.author} - {self.tag} - {self.is_published}'
