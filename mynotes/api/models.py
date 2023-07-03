from typing import Any
from django.db import models

# Create your models here.
class Note(models.Model):
    body=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]