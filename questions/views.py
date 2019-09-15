from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

from accounts.models import Profile, User
from accounts.forms import ProfileForm, UserForm


#   question set -> 1, 2~,      questions -> 01, 02 ~
@login_required()
def question_set_1(request, user_id):
    if request.method == 'POST':
        question_01 = request.POST.get('question_01', "")
        question_02 = request.POST.get('question_02', "")
        question_03 = request.POST.get('question_03', "")
        if question_01 == "" or question_02 == "" or question_03 == "":   #checkbox 체크 안하면 에러메세지 나오고 다시 같은 페이지 표시 하는 것.
            messages.info(request, 'Please select all answer for each questions!')
            return HttpResponseRedirect('/questions/question_set_1/'+str(user_id))
        user = get_object_or_404(User, pk=user_id) 
        user.profile.question_01 = question_01
        user.profile.question_02 = question_02
        user.profile.question_03 = question_03
        #fixed from "user.profile.save()" for getting some benefit
        user.profile.save(update_fields=['question_01', 'question_02', 'question_03'])
        return render(request, 'question_set_2.html', {'user': user} )
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'question_set_1.html', {'error': 'Please select all answer for each questions.', 'user': user})

@login_required()
def question_set_2(request, user_id):
    if request.method == 'POST':
        question_04 = request.POST.get('question_04', "")
        question_05 = request.POST.get('question_05', "")
        question_06 = request.POST.get('question_06', "")
        if question_04 == "" or question_05 == "" or question_06 == "":   #checkbox 체크 안하면 에러메세지 나오고 다시 같은 페이지 표시 하는 것.
            messages.info(request, 'Please select all answer for each questions!')
            return HttpResponseRedirect('/questions/question_set_2/'+str(user_id))
        user = get_object_or_404(User, pk=user_id) 
        user.profile.question_04 = question_04
        user.profile.question_05 = question_05
        user.profile.question_06 = question_06
        user.profile.save(update_fields=['question_04', 'question_05', 'question_06'])
        return render(request, 'question_set_3.html', {'user': user} )
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'question_set_2.html', {'error': 'Please select all answer for each questions.', 'user': user})

@login_required()
def question_set_3(request, user_id):
    if request.method == 'POST':
        question_07 = request.POST.get('question_07', "")
        question_08 = request.POST.get('question_08', "")
        question_09 = request.POST.get('question_09', "")
        if question_07 == "" or question_08 == "" or question_09 == "":   #checkbox 체크 안하면 에러메세지 나오고 다시 같은 페이지 표시 하는 것.
            messages.info(request, 'Please select all answer for each questions!')
            return HttpResponseRedirect('/questions/question_set_3/'+str(user_id))
        user = get_object_or_404(User, pk=user_id) 
        user.profile.question_07 = question_07
        user.profile.question_08 = question_08
        user.profile.question_09 = question_09
        user.profile.save(update_fields=['question_07', 'question_08', 'question_09'])
        return render(request, 'question_set_4.html', {'user': user} )
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'question_set_3.html', {'error': 'Please select all answer for each questions.', 'user': user})

@login_required()
def question_set_4(request, user_id):
    if request.method == 'POST':
        question_10 = request.POST.get('question_10', "")
        question_11 = request.POST.get('question_11', "")
        question_12 = request.POST.get('question_12', "")
        if question_10 == "" or question_11 == "" or question_12 == "":   #checkbox 체크 안하면 에러메세지 나오고 다시 같은 페이지 표시 하는 것.
            messages.info(request, 'Please select all answer for each questions!')
            return HttpResponseRedirect('/questions/question_set_4/'+str(user_id))
        user = get_object_or_404(User, pk=user_id) 
        user.profile.question_10 = question_10
        user.profile.question_11 = question_11
        user.profile.question_12 = question_12
        user.profile.save(update_fields=['question_10', 'question_11', 'question_12'])
        return render(request, 'question_set_5.html', {'user': user} )
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'question_set_4.html', {'error': 'Please select all answer for each questions.', 'user': user})

@login_required()
def question_set_5(request, user_id):
    if request.method == 'POST':
        question_13 = request.POST.get('question_13', "")
        question_14 = request.POST.get('question_14', "")
        question_15 = request.POST.get('question_15', "")
        if question_13 == "" or question_14 == "" or question_15 == "":   #checkbox 체크 안하면 에러메세지 나오고 다시 같은 페이지 표시 하는 것.
            messages.info(request, 'Please select all answer for each questions!')
            return HttpResponseRedirect('/questions/question_set_5/'+str(user_id))
        user = get_object_or_404(User, pk=user_id) 
        user.profile.question_13 = question_13
        user.profile.question_14 = question_14
        user.profile.question_15 = question_15
        user.profile.done = True
        user.profile.save(update_fields=['question_13', 'question_14', 'question_15', 'done'])
        return redirect('loading', user_id)    ###result로 가고 저장도 따로 해주고 해야함
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'question_set_5.html', {'error': 'Please select all answer for each questions.', 'user': user})
