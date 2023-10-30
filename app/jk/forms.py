from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MeterReading
from .models import User
from django.contrib.auth.forms import AuthenticationForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    full_name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=15)
    apartment_number = forms.CharField(max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "full_name",
                  "phone_number", "apartment_number")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.apartment_number = self.cleaned_data['apartment_number']

        if commit:
            user.save()
        return user


class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ["hot_water_reading", "cold_water_reading", "gas_reading", "electricity_reading"]


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Введите email')
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)


