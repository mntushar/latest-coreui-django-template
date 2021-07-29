from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*


#user loging
def user_loging(request):
    loging_form = UserLogingForm()
    if request.method == 'POST':
        loging_form = UserLogingForm(request.POST)
        if loging_form.is_valid():    
            name = loging_form.cleaned_data['name']
            password = loging_form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_loging = 'The email and password that you entered did not match our records. Please double-check and try again.'
                context = {
                    'loging_form':loging_form,
                    'error_loging':error_loging,
                }
                return render(request, 'login/user_login.html', context)
    context = {
        'loging_form':loging_form
    }
    return render(request, 'login/user_login.html', context)


#user logout
def user_logout(request):
    logout(request)
    return redirect('/')


#add user
def adduser(request):
    user_forms = UserInfoForm()
    password_forms = UserPassForm()
    if request.method == 'POST':
        user_forms = UserInfoForm(request.POST)
        password_forms = UserPassForm(request.POST)
        if user_forms.is_valid() and password_forms.is_valid():
            p = password_forms.cleaned_data['password']
            rp = password_forms.cleaned_data['repassword']
            email = user_forms.cleaned_data['email']
            if p==rp:
                user_forms_obj = user_forms.save(commit=False)
                user_pass_obj = User.objects.create_user(username=email, password=p, email=email)
                user_forms_obj.password = user_pass_obj
                user_forms.save()
                user = UserInfo.objects.get(email=email)
                context = {
                    'user_info':user,
                }
                return render(request, 'login/user_save_conformation.html', context)


    context = {
        'user_forms' : user_forms,
        'password_forms' : password_forms,
    }
    return render(request, 'login/add_user_forms.html', context)


#user profile
@login_required
def profileuser(request):
    user = request.user
    email = user.username
    userinfo = UserInfo.objects.get(email=email)
    context = {
       'userinfo':userinfo, 
    }
    return render(request, 'login/user_profile.html', context)


#change password of user
@login_required
def passchange(request):
    user = request.user
    pass_forms = UserPassChangeForm()
    if request.method == 'POST':
        pass_forms = UserPassChangeForm(request.POST)
        if pass_forms.is_valid():
            newp = pass_forms.cleaned_data['password']
            newrp = pass_forms.cleaned_data['repassword']
            if newp == newrp:
                username = user.username
                user = User.objects.get(username=username)
                user.set_password(newp)
                user.save()
                return redirect('home-deshboard')
    context = {
        'pass_forms':pass_forms,
    }
    return render(request, 'login/change_pass.html', context)


#edit user profile
@login_required
def editprofile(request):
    user = request.user
    email = user.username
    userinfo = UserInfo.objects.get(email=email)
    edit_forms = UserInfoForm(instance=userinfo)
    if request.method == 'POST':
        edit_forms = UserInfoForm(request.POST, instance=userinfo)
        if edit_forms.is_valid():
            edit_forms.save()
            return redirect('user-profile')
    context ={
        'edit_forms':edit_forms,
    }
    return render(request, 'login/profile_edit.html', context)

