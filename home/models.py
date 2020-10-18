from django.db import models

# Create your models here.



class postform(models.Model):
    author = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.author
