from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    expired_at = models.DateField()

    def __str__(self) -> str:
        return self.title