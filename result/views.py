from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Profile, User
from accounts.forms import ProfileForm, UserForm
# Create your views here.
@login_required()
def loading(request, user_id):
    user = get_object_or_404(User, pk=user_id) 
    my_link = request.build_absolute_uri('/') + str(user_id)
    if user.profile.link_from is not None:
        link_from = user.profile.link_from
        user.profile.done = True
        user.profile.save(update_fields=['done'])
        try:
            from_user = User.objects.get(id=int(link_from))
        except  User.DoesNotExist:
            render(request, 'main.html', {'user': user, "my_link": my_link, 'link_from': link_from}) ####이거 수정 필요
        return render(request, 'result.html', {'user': user, "my_link": my_link, 'link_from': link_from, "from_user": from_user,})
    return render(request, 'result.html', {'user': user, "my_link": my_link, 'link_from': None})

@login_required()
def result(request, user_id):
    pass