from django.contrib import admin
from .models import User, Video, Channel, Image, Comment

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'date_of_birth', 'gender')
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):   
    list_display=('title', 'description', 'category', 'upload')
    actions = ['approve_videos']
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('title', 'picture')
    actions = ['approve_images']
   
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'commenting', 'active')
    actions = ['approve_comments']
    