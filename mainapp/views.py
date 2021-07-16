from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls import reverse


def adminLogin(request):
    return render(request, "admin_templates/signin.html")

def adminLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("admin_login"))

