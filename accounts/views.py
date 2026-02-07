from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout 
from .forms  import UserRegistrationForm,  UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username,email=email,password=password)
            login(request, user)
            return redirect('job_list')
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html",{"form":form})

def login_view(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username,email =email, password =password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.POST.get("next") or "job_list"
            return redirect('job_list')
        else:
            error_message = "Invalid Credentials !"
    return render(request,"accounts/login.html",{"error": error_message})

def logout_confirm_view(request):
    return render(request, "accounts/logout_confirm.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('job_list')

@login_required
def profile_view(request):
    user = request.user

    # If profile already complete, you can let them still edit, otherwise force completion
    if not user.first_name or not user.last_name or not user.profile.profile_image:
        force_complete = True
    else:
        force_complete = False

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("job_list")  # after completion, redirect to home

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)

    return render(request, "accounts/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "force_complete": force_complete
    })

def custom_404_view(request, exception):
    return render(request, "Error_Page/404.html", status=404)