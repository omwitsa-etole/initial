from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Video, Channel, User, Image, Comment, Question
from .forms import VideoForm, ImageForm, SignUpForm
from .forms import LoginForm, CommentForm, QuestionForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import login, authenticate

def log_in(request):
    error = '';
    username = 'not logged in'
    video_list = Video.objects.all()
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
  
        if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         password = MyLoginForm.cleaned_data['password']
         user = authenticate(username=username, password=password)
         if user:
             login(request, user)
             request.session['username'] = username
             return render(request, 'indexhome.html', locals())
         else: 
            error = 'invalid username or passord';
       
    else:
      MyLoginForm = LoginForm()
        
    return render(request, 'login.html', locals())
    
def formView(request):
    error = '';
    search_query = request.GET.get('search')
    if request.session.has_key('username'):
        username = request.session['username']
        if search_query:
            video_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
        else:
            video_list = Video.objects.all().order_by("-date_created")
        index = 0
    else:
        return render(request, 'login.html', {"error_log":error})
        
    return render(request, 'indexhome.html', locals())

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong><a href='/video/in/'>login </a>")
  
def SignUpView(request):
    error = ''
    new_user = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            error = 'Account Created Successfully'
        else:
            error = 'Failed To create Account Please try again'
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', locals())
def SaveVideo(request):
    
    
    if saved == True:
        return HttpResponse("<strong>File Uploaded Succesfully.</strong><br><a href='/video/in/upload/'>back</a>")
    else:
        return HttpResponse("<strong>Failed.</strong><br><a href='/video/in/upload/'>back</a>")
    
class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'details.html'
    
def IndexView(request):
    username = 'not loged in'
    search_query = request.GET.get('search')
    if search_query:
        video_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
    else:
        video_list = Video.objects.all().order_by("-date_created")
    return render(request, 'index.html', {"username" : username, "video_list": video_list})

def UploadView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        query = get_object_or_404(User)
        saved = False
        error = ''
        new_video = None
        if request.method == "POST":
            MyVideoForm = VideoForm(request.POST, request.FILES)
            if MyVideoForm.is_valid():
                new_video = MyVideoForm.save(commit=False)
                new_video.query = query
                new_video.save()
                saved = True
                success = 'Video Uploaded success'
        else:
            MyVideoForm = VideoForm()
         
    else:
        return render(request, 'login.html', {})
      
    return render(request, 'upload.html', locals())
class VideoDetailOutView(generic.DetailView):
    model = Video
    context_object_name = 'query'
    template_name = 'video_detail_out.html'
    
class ImageDetailOutView(generic.DetailView):
    model = Image
    context_object_name = 'query'
    template_name = 'image_detail_out.html'

def VideoDetailView(request, pk):
    template_name = 'video_detail.html'
    query = get_object_or_404(Video, pk=pk)
    video_list = Video.objects.all().order_by("-date_created")
    comments = Comment.objects.all()
    new_comment = None
    username = request.session['username']
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.query = query
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, locals())
    
def ImageDetailView(request, pk):
    template_name = 'image_detail.html'
    query = get_object_or_404(Image, pk=pk)
    comments = Comment.objects.all()
    new_comment = None
    username = request.session['username']
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.query = query
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, locals())
    
   
def SaveImage(request):
    if request.session.has_key('username'):
        username = request.session['username']
        saved = False
        new_image = None
        if request.method == "POST":
            MyImageForm = ImageForm(request.POST, request.FILES) 
            if MyImageForm.is_valid():
                new_image = MyImageForm.save(commit=False)
                new_image.save()
                saved = True
            else:
                MyImageForm = ImageForm()
    else:
        return render(request, 'login.html', {})
        
    return render(request, 'upload2.html', locals())
  
def Settings(request):
    if request.session.has_key('username'):
         username = request.session['username']
         return render(request, 'settings.html', {"username" : username})
    else:
      return render(request, 'login.html', {})
def PassView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'pass_set.html', {"username" : username})
    else:
        return render(request, 'login.html', {})
def DetailView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user = User.objects
        return render(request, 'details.html', {"username" : username,"user":user})
    else:
        return render(request, 'login.html', {})
def ImageView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        search_query = request.GET.get('search') 
        if search_query:
            image_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
        else:
            image_list = Image.objects.all().order_by("-date_created")
    else:
        return render(request, 'login.html', {}) 
        
    return render(request, 'images.html', {"username" : username,"image_list":image_list})
def ImageOutView(request):
    username = "not logged in"
    search_query = request.GET.get('search') 
    if search_query:
        image_list = Image.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
    else:
        image_list = Image.objects.all().order_by("-date_created")
        
    return render(request, 'images_out.html', {"username" : username,"image_list":image_list})
def QuestionView(request):
    error = '';
    search_query = request.GET.get('search')
    if request.session.has_key('username'):
        username = request.session['username']
        new_question = None
        if search_query:
            question_list = Question.objects.filter(Q(question__icontains=search_query) & Q(more_description__icontains=search_query)).order_by("-date_created")
        else:
            question_list = Question.objects.all().order_by("-date_created")
        index = 0
        if request.method == "POST":
            MyQuestionForm = QuestionForm(request.POST, request.FILES) 
            if MyQuestionForm.is_valid():
                new_question.save()
                saved = True
            else:
                MyQuestionForm = QuestionForm()
    else:
        return render(request, 'login.html', {"error_log":error})
        
    return render(request, 'questions.html', locals())
def QuestionOutView(request):
    error = '';
    search_query = request.GET.get('search')
    username = "not logged in"
    if search_query:
        question_list = Question.objects.filter(Q(question__icontains=search_query) & Q(more_description__icontains=search_query)).order_by("-date_created")
    else:
        question_list = Question.objects.all().order_by("-date_created")
    index = 0
    
    return render(request, 'questionsout.html', locals())
    
def QuestionDetailView(request, pk):
    template_name = 'q&adetail.html'
    question = get_object_or_404(Question, pk=pk)
    answers = Comment.objects.all()
    new_answer = None
    username = request.session['username']
    
    if request.method == 'POST':
        answer_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_answer = comment_form.save(commit=False)
            new_answer.question = question
            new_answer.save()
    else:
        answer_form = CommentForm()
        
    return render(request, template_name, locals())
class QuestionDetailOutView(generic.DetailView):
    model = Question;
    context_object_name = "question";
    template_name = "q&adetailout.html"
def ForgotPass(request):
        return render(request, 'password_reset.html', {})
class ChannelDetailView(generic.DetailView):
    model = Channel
    
class UploadsListView(generic.ListView):
    model = Video

