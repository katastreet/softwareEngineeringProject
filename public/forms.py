from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from public.models import OfficeData


#  example of exending our user form
class MyRegistrationForm(UserCreationForm):
    emails = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()


# example of our own form
class OfficeForm(forms.ModelForm):
    class Meta:
        model = OfficeData
        fields = '__all__'
