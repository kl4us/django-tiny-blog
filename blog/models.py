from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, db_index=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField(blank=True, help_text="The body of the Post")
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    previous_post = models.ForeignKey('self', related_name='previous', null=True, blank = True)
    next_post = models.ForeignKey('self', related_name='next', null=True, blank = True)
    
    class Meta:
         ordering = ["-insert_date"]  

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return unicode(self.title)     

    def was_published(self):
        return self.approved
    was_published.admin_order_field = 'update_date'
    was_published.boolean = True
    was_published.short_description = 'Published?' 