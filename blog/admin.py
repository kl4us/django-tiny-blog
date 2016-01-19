from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post

class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"slug":("title",)}
    list_display = ('title', 'was_published', 'insert_date', 'update_date')
    list_filter = ['insert_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)