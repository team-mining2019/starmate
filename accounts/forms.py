from django import forms
from django.contrib.auth import get_user_model

from .models import Profile, User

#User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username',]:
            self.fields[fieldname].help_text = None

    #def clear_username(self):
    #    username = self.cleaned_data['username']
    #    if User.objects.filter(username=username).exists():
    #        raise form.ValidationError("Username is already exist")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('link_from',)