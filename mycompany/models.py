from django.db import models
from django.contrib.auth.models import User
import datetime
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    Property_CHOICES = [
        ('RP', 'Resendential Project'),
        ('HS', 'Housing Society'),
        ('RSK', 'Real Estate Knowledge'),
        ('CU', 'Construction Update'),
    ]

    Id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    Posted_by = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField(("Date"), default=datetime.date.today)
    content = RichTextField()
    category=models.CharField(choices=Property_CHOICES,max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title

class Images(models.Model):
    note = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',null=True,blank=True)

