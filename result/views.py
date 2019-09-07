from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Profile, User
from accounts.forms import ProfileForm, UserForm
# Create your views here.
@login_required()
def loading(request, user_id):
    user = get_object_or_404(User, pk=user_id) 
    my_link = request.build_absolute_uri('/') + str(user_id)
    
    return render(request, 'result.html', {'user': user, "my_link": my_link})

@login_required()
def result(request, user_id):
    pass