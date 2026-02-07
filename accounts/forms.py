from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget = forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(label="Email", widget = forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"class":"form-control"}))
    password_confirm = forms.CharField(label="Confirm Password", widget = forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username","email","password","password_confirm"]
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Password do not match!")
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget = forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(label="Email", widget = forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", widget = forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", widget = forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class ProfileUpdateForm(forms.ModelForm):
    profile_image= forms.ImageField(label="Profile Image", widget = forms.ClearableFileInput(attrs={"class":"form-control"}))
    middle_name = forms.CharField(label="Middle Name", widget = forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Profile
        fields = ["profile_image", "middle_name"]