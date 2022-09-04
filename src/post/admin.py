from django.contrib import admin
from post.models import (PostModel,
                        PostImageModel)

class PostImagesAdmin(admin.StackedInline):
    model = PostImageModel

@admin.register(PostModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImagesAdmin]