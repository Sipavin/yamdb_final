from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from categories.models import Title
from users.models import Users


class Review(models.Model):
    """Reviews of titles. The review is tied to a specific title."""
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        unique_together = ('title', 'author')
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    """Comments on reviews. The comment is linked to a specific review."""
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name='Отзыв'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
