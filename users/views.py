# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from index import views as index
from users import forms
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib import messages

@sensitive_post_parameters('password')
def connect(request):

    if request.user.is_authenticated():
        return redirect(index.home)

    if(request.method == "POST"):
        form = forms.ConnectForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
            if user:
                login(request,user)
                if user.first_name:
                    messages.success(request,"Bonjour "+user.first_name)
                else:
                    messages.success(request,"Bonjour "+user.username)
                return redirect(index.home)
            else:
                error = True
    else :
        form = forms.ConnectForm()

    return render(request,"users/connect.html",locals())

def disconnect(request):

    if not request.user.is_authenticated():
        return redirect(connect)

    if(request.method == "POST"):
        if request.user.first_name:
            messages.success(request,"Au revoir "+request.user.first_name)
        else:
            messages.success(request,"Au revoir "+request.user.username)
        logout(request)
        return redirect(index.home)

    return render(request,"users/disconnect.html",locals())