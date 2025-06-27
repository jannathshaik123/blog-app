from django.contrib import admin
from .models import CustomUser, Post
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','bio', 'profile_picture', 'twitter', 'facebook', 'instagram', 'linkedin')

admin.site.register(CustomUser, CustomUserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_published')
    ordering = ('-created_at',)
admin.site.register(Post, PostAdmin)
