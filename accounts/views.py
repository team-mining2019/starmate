from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404
from django.contrib import messages

from .models import Profile, User
from .forms import ProfileForm, UserForm




def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        #uesrname_temp = UserForm(request.POST).username
        #if form.filter(username=self.cleaned_data['username']).exists():
        #    return render(request, 'signup.html', {'error': 'username is already exist.'})

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            profile = Profile(user=new_user)
            profile.save()
            auth.login(request, new_user)
            context = {'form': form, 'user': new_user,}
            if profile.done is True:
                return render(request, 'result.html', context)
            return render(request, 'question_set_1.html', context)

        #messages.error(request,'Username is already exist!')
        return render(request, 'signup.html', {'form': form, 'flag': True}) ###이거 예외 처리해야함 (뭐냐면 아이디 중복, 아이디 만들었는데 로그인안하고 사인업해버릴 때.)
    else:
        form = UserForm()
        context = {'form': form,}
        return render(request, 'signup.html', context)
    


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                user = User.objects.get(pk=user.id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
            context = {'user': user}
            ###from link저장 필요, done이 true면 안하고 바로 result로 넘어가게.
            if user.profile.done is True:
                return render(request, 'result.html', context)
            return render(request, 'question_set_1.html', context)
        else:
            return render(request, 'login.html', {'form': form, 'error': 'username or password is incorrect.', 'flag2': True})
    else:
        form = UserForm()
        context = {'form': form,}
        return render(request, 'login.html', context)


def logout(request): 
    auth.logout(request)
    return redirect('main')


def signup_from(request, from_user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        #uesrname_temp = UserForm(request.POST).username
        #if form.filter(username=self.cleaned_data['username']).exists():
        #    return render(request, 'signup.html', {'error': 'username is already exist.'})

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            profile = Profile(user=new_user)
            profile.link_from = str(from_user_id)
            profile.save()
            auth.login(request, new_user)
            context = {'form': form, 'user': new_user, "from_user_id": from_user_id,}
            if profile.done is True:
                return render(request, 'result.html', context)
            return render(request, 'question_set_1.html', context)

        #messages.error(request,'Username is already exist!')
        return render(request, 'signup_from.html', {'form': form, 'flag': True}) ###이거 예외 처리해야함 (뭐냐면 아이디 중복, 아이디 만들었는데 로그인안하고 사인업해버릴 때.)
    else:
        form = UserForm()
        context = {'form': form, "from_user_id": from_user_id,}
        return render(request, 'signup_from.html', context)



def login_from(request, from_user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                user = User.objects.get(pk=user.id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
            user.profile.link_from = str(from_user_id)
            #user.save()
            user.profile.save()
            context = {'user': user, "from_user_id": from_user_id,}
            ###from link저장 필요, done이 true면 안하고 바로 result로 넘어가게.
            if user.profile.done is True:
                return render(request, 'result.html', context)
            return render(request, 'question_set_1.html', context)
        else:
            return render(request, 'login_from.html', {'form': form, 'error': 'username or password is incorrect.', 'flag2': True})
    else:
        form = UserForm()
        context = {'form': form, "from_user_id": from_user_id,}
        return render(request, 'login_from.html', context)
