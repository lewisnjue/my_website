from django.shortcuts import render,redirect
from .forms import Register,PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as user_logout, authenticate, login
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def home(request):
        if request.user.is_authenticated:
            post = Post.objects.all()
            return render(request, 'main/home.html',{
                'posts':post
            })
        else:
            return HttpResponseRedirect(reverse('login'))



def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = Register()
    return render(request, 'main/register.html', {'form': form})

def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Use appropriate form name
        if form.is_valid():
            post = form.save(commit=False)  # Prevent immediate saving
            post.user = request.user  # Associate post with logged-in user
            post.save()
            return redirect('home')  # Redirect to desired page after successful creation
    else:
        form = PostForm()  # Use appropriate form name
        return render(request, 'main/post.html', {'form': form})
    

def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    # Check if user is authenticated and authorized to delete the post
    if not request.user.is_authenticated or post.user != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return HttpResponseRedirect(reverse('home'))  # Redirect back to the home page

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return HttpResponseRedirect(reverse('home'))

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/profile.html',{
        'profile': profile
    })