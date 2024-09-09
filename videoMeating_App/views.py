from django.shortcuts import render,redirect
from videoMeating_App.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request,"home.html")


def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error_message=form.errors.as_text
            return render(request,'register.html',{"msg":error_message})
    return render(request,'register.html')

def login_view(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashbord")
        else:
            return render(request,'login.html',{"msg":"Invalid credentials. Please Try again.."})
    return render(request,'login.html')

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="login")
def dashbord(request):
    return render(request,'dashbord.html')

@login_required(login_url="login")
def videoMeeting_view(request):
    return render(request,'videoMeeting.html',{"user":request.user.first_name})

@login_required(login_url="login")
def join_room_view(request):
    if request.method=="POST":
        roomID=request.POST['roomid']
        return redirect('/videocall?roomID='+ roomID)
    return render(request,'join_room.html')
