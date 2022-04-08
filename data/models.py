from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
    
class Video(models.Model):
    upload = models.FileField(upload_to = 'videos/')
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField(help_text="Video Description", null=True, blank=True)
    category=models.CharField(max_length=100, help_text="Enter Video Category", null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _str_(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.id)])
        
    def get_another_url(self):
        return reverse('video_detail_out', args=[str(self.id)])
      
    
    class Meta:
      db_table = "video"

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50,null=False, blank=False,default="")
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length = 100, default="", null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10,choices=gender_choice, null=False, blank=False)
    
    
    def get_absolute_url(self):
        return reverse('upload_detail', args=[str(self.id)])
        
    def _str_(self):
        return f'{self.last_name}, {self.first_name}'

class Question(models.Model):
    question = models.CharField(max_length = 300,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    more_description = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "question"
        
    def _str_(self):
        return self.question
    def get_absolute_url(self):
        return reverse('questions_url_in', args=[str(self.id)])
    def get_another_url(self):
        return reverse('questions_url_out', args=[str(self.id)])

class Comment(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments', null=True, blank=True)
    commenting = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_on']
        
    def _str_(self):
        return 'comment {}'.format(self.commenting)
      
class Image(models.Model):
    title = models.CharField(max_length = 50, null=False, blank=False)
    picture = models.FileField(upload_to = 'pictures/')
    description=models.TextField(help_text="image Description", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
    class Meta:
        db_table = "image"
   
class Channel(models.Model):
    def _str_(self):
        return self.channel_name
        
    def get_absolute_url(self):
        return reverse('channel-detail', args=[str(self.id)])
