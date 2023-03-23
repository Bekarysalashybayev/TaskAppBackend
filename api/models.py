from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
