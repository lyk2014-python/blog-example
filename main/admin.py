from django.contrib import admin

from main.models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["title"]
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
