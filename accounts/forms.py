from django import forms

from .models import Profile, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username',]:
            self.fields[fieldname].help_text = None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('link_from',)