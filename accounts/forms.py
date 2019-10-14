from django.contrib.auth import forms

from . import models


class UserCreateForm(forms.UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = models.User

    def __inti__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email address'
