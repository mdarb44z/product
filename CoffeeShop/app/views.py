from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# from .models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def products(request):
    return render(request,'products.html')

def review(request):
    return render(request,'review.html')


def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')



def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        conformpassword=request.POST.get('pass2')
        
        if(password!=conformpassword):
            messages.warning(request,"Password is incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
                messages.error(request,"Username Is Taken")
                return redirect('/signup')
        except:
            pass
        
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/signup')
        except:
            pass
        
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Successful please Login")
        return redirect('/login')
    return render(request,'signup.html')

def handlelogin(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('pass1')
        myuser=authenticate(username=uname,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Wrong Credentias")
            return redirect('/login')
     return render(request,'login.html')
 
def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successful")
    return redirect('/login')
