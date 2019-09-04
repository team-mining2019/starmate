from django.shortcuts import render
from accounts.forms import UserForm, ProfileForm


def main(request):
    return render(request, 'main.html')