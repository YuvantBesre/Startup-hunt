from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    publication_date = models.DateField()
    Votes = models.IntegerField(default=1)
    Image = models.ImageField(upload_to='images/')
    Icon = models.ImageField(upload_to='images/')
    content = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def SummaryOfContent(self):
        return self.content[:200]

    def __str__(self):
        return self.title

