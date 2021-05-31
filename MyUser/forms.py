from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'sex', 'phone_number', 'date_of_birth', 'school', 'image', 'password')



    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
