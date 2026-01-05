from django.contrib import admin

from blog.models import Tag, Post

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag__title', 'author', 'is_published')
    list_filter = ('tag__title', 'author', 'is_published')
