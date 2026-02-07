from django.db import models


class Review(models.Model):
    """Модель отзыва."""

    name = models.CharField(
        max_length=100,
        verbose_name='ФИО',
    )
    star = models.FloatField(
        default=5.00,
        verbose_name='Оценка',
    )
    aim = models.CharField(
        max_length=150,
        verbose_name='Цель занятий',
    )
    review = models.TextField(
        verbose_name='Текст отзыва',
    )
    date = models.DateField(
        verbose_name='Дата публикации отзыва',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовать'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
    def __str__(self):
        return f'{self.name} - {self.star} - {self.date} - {self.is_published}'
