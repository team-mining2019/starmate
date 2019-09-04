from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404

from .models import Profile, User
from .forms import ProfileForm, UserForm

# 다시 고쳐야할듯

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            profile = Profile(user=new_user)
            profile.save()
            auth.login(request, new_user)

            context = {'form': form, 'user': new_user,}
            return render(request, 'question_set_1.html', context)
        return render(request, 'signup.html') ###이거 예외 처리해야함 (뭐냐면 아이디 중복, 아이디 만들었는데 로그인안하고 사인업해버릴 때.)
    else:
        form = UserForm()
        context = {'form': form,}
        return render(request, 'signup.html', context)
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
            context = {'form': form, 'user': user}
            return render(request, 'question_set_1.html', context)
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        form = UserForm()
        context = {'form': form,}
        return render(request, 'login.html', context)


def logout(request): #이건 if request.method == 'POST': 이거 필요 없다!!!
    auth.logout(request)
    return redirect('main')