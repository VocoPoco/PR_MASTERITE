from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    first = forms.CharField(max_length=255)
    last = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255)
    # type = forms.BooleanField(default=False)

    class Meta:
        model = User
        fields = ("username", "first", "last", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user