from django.shortcuts import redirect, render
from authe.forms import SignUpForm
# Create your views here.
def login(request):
    return render(request,'authe/login.html')
def register(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    
    fm = SignUpForm()
    return render(request, 'authe/signup.html',{'fm':fm})