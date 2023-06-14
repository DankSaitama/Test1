from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

#Register User
from django.contrib.auth.forms import UserCreationForm


def register_user(request):
    if request.method=='POST':
        fn=UserCreationForm(request.POST)
        if fn.is_valid():
            uname=fn.cleaned_data['username']
            upass=fn.cleaned_data['password1']
            u1=User.objects.create(username=uname,password=upass)
            u1.save()
            return redirect('success')
    else:
        fn = UserCreationForm()
        return render(request,'register.html',{'form':fn})

