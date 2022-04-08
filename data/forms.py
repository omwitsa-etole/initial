from django import forms
from .models import User, Comment, Video, Image, Question
   
class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
   
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('upload','title','description')
      
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('picture','title','description')
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenting',)
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','more_description')