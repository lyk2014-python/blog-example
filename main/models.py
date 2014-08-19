from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tag")
    author = models.ForeignKey(User)

    def __unicode__(self):
        return smart_unicode(self.title)


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return smart_unicode(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return smart_unicode(self.name)

