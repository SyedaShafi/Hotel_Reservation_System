from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import UserAccounts

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female')
)



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_TYPE) 
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        gender  = cleaned_data.get("gender")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")      
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False  
        if commit:
            user.save()
            account_no = 10000 + user.id
            user_account = UserAccounts.objects.create(user = user, gender=self.cleaned_data['gender'], account_no = account_no)

        user_account.save()
        return user
    

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
   