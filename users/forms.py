from django.forms import ModelForm
from .models import CustomUser
from django import forms
from allauth.account.forms import SignupForm
from django import forms
from allauth.account.adapter import DefaultAccountAdapter

class UserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            #'username',
            'bio',
        ]

    def __init__(self, #username=None,
     bio=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        #if username:
            #self.fields['username'].widget.attrs['value'] = username
        if bio:
            self.fields['bio'].widget.attrs['value'] = bio

    def update(self, user):
        #user.username = self.cleaned_data['username']
        user.bio = self.cleaned_data['bio']
        user.save()

class CustomSignupForm(SignupForm):
    age = forms.IntegerField()

    class Meta:
        model = CustomUser