from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    return render(request, "app/home.html")

#! we are gonna use decorater to see specific views

@login_required
def special(request):
    return render(request,'app/special.html')


def register(request):
    
    if request.method == 'POST':
        #? pass post data to instantiate the form
        form = UserCreationForm(request.POST);
        
        if form.is_valid():
            #? after validation give an authoriation
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password1']
             # inspect the page and see the first password is password1, import authenticate
            #user = authenticate(username=username, password=password)
            #! i already have the user when I save the form, do not need to authenticate since
            #! I already provide it when calling login()
            user=form.save();
            #? login after registration
            login(request,user)
            return redirect('/')
    
    else:
        #? just view the form
        form = UserCreationForm()

    context = {
        'form': form
    }
    
    return render(request,'registration/register.html',context)