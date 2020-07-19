from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'sorry username already exist')
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.error(request, "sorry email already exist")
            return redirect('signup')

        else:
        
            user= User.objects.create_user(username=username, email=email,password=password)
            user.save()
            print("user created")
            messages.success(request, f"Account created for {username}")
            return redirect('signin')

    else:
        return render(request, 'signup.html')


    

def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username ,password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:

                return redirect('/')
        else:
            messages.error(request,"invalid username ")
            return redirect('signin')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')







    
