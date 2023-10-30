from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserAuthenticationForm, MeterReadingForm, RegistrationForm
from django.contrib import messages
from .models import MeterReading


def Home(request):
    return render(request, "jk/home.html")


def About(request):
    return render(request, "jk/about.html")


def Personal_Area(request):
    return render(request, "jk/personal_area.html")


def Editing_profile(request):
    return render(request, "jk/editing_profile.html")


def Sing_up(request):
    return render(request, "jk/sing_up.html")


def Login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('personal_area')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = CustomUserAuthenticationForm()
    return render(request = request, template_name = "jk/login.html", context={"login_form":form})


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/personal_area')
    else:
        form = RegistrationForm()

    return render(request, 'jk/sing_up.html', {'form': form})



@login_required
def meter_reading_submit(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            meter_reading = form.save(commit=False)
            meter_reading.user = request.user
            meter_reading.save()
            return redirect('personal_area')
    else:
        form = MeterReadingForm()
    return render(request, "jk/entering_readings.html", {"form": form})
