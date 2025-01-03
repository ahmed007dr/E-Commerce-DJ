from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import SignupForm,UserActivateForm
from .models import Profile
# Create your views here.
from django.core.mail import send_mail

def signup(request):  # Fixed spelling from 'singup' to 'signup'
    '''
    - create new user
    - send email : code 
    - redirect
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] # fetch user & email to un activate
            email = form.cleaned_data['email']

            user = form.save(commit=False) # un activate 
            user.is_active = False

            form.save() # after this step >>> will create signal recver profile
            profile = Profile.objects.get(user__username=username)# move from profile to user user__username 
            #send email 
            send_mail(
                "acctivate your account",
                f"welcome {username}./nUser this code {profile.code} to activate your account",
                "ahmed.tamem.eg@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(request,f'accounts/{username}/activate')


        
    else :
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_activate(request):
    '''
    - code -----> activate
    - redirect -----> login
    '''
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        # Add your form handling logic here
    else :
        form = UserActivateForm()
    return render(request, 'accounts/signup.html', {'form': form})
