from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import View
from .forms import LoginForm, SignUpForm


class LoginPageView(View):
    template_name = "authentication/login.html"

    def get(self, request):
        print("Requête GET reçue")
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        print("Requête POST reçue")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User is authenticated:", request.user.is_authenticated)
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, self.template_name, {"form": form})


def signin_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("authentication:login"))
    else:
        form = SignUpForm()
    return render(request, "authentication/signup.html", {"form": form})
