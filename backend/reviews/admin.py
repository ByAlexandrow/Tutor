from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'star', 'date', 'is_published')
    list_filter = ('date', 'is_published')
