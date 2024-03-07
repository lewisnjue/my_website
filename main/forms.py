from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Post
from .models import Profile

class Register(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specify the model to associate the form with
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Add any custom form fields, widgets, or validation logic here
class User_updateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')
class Profile_updateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    
    
    