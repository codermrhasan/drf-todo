from django.db import models


class Todo(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='todos', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
