from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    address = models.TextField()
    postcode = models.TextField()
    description = models.TextField(default='')
    #more fields
    def __unicode__(self):
        return self.address

class Review(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField(max_length=1000)
    title = models.TextField(max_length=100)
    date = models.DateField(auto_now=True)
    subject = models.ForeignKey(Property)
    
    def __unicode__(self):
        return unicode(self.author) + ": " + self.body

    