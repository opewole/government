from django.db import models


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    name = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name[:50]
