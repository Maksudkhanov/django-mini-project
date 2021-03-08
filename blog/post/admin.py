from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created', 'updated', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    list_editable = ('published',)


admin.site.register(Post, PostAdmin)