from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):
    template_name = "login.html"


# Create your views here.

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")

    else:

        user_form = UserCreationForm()
    return render (request, "register.html", {"user_form": user_form})

