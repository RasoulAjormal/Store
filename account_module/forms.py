from django import forms
from django.core.exceptions import ValidationError

from account_module.models import SingInModel, LogInModel, User


class LogInForm(forms.ModelForm):
    class Meta:
        model = LogInModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'پسورد'}),
        }
        labels = {
            'username': 'نام کاربری',
            'password': 'پسورد'
        }
        error_messages = {
            'username': {
                'required': 'نام کاربری اشتباه است'
            },
            'password': {
                'required': 'پسورد اشتباه است'
            }
        }


class SingInForm(forms.ModelForm):
    class Meta:
        model = SingInModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'پسورد'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'تکرار پسورد'}),
        }
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'password': 'پسورد',
            'confirm_password': 'تکرار پسورد'
        }
        error_messages = {
            'username': {
                'required': 'نام کاربری صحیح وارد کنید'
            },
            'email': {
                'required': 'ایمیل صحیح وارد کنید'
            },
            'password': {
                'required': 'پسورد صحیح وارد کنید'
            },
            'confirm_password': {
                'required': 'تکرار پسورد صحیح وارد کنید'
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('ایمیل وارد شده تکراری می باشد.')
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username):
            raise ValidationError('نام کاربری وارد شده تکراری می باشد.')
        else:
            return username

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('پسورد با تکرار پسور مغایرت دارد')


class ForgetPasswordForm(forms.ModelForm):
    class Meta:
        model = SingInModel
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل'})
        }
        labels = {'email': 'ایمیل'}
        error_messages = {'email': {'required': 'ایمیل اشتباه می باشد.'}}


class ResetPasswordForm(forms.ModelForm):
    class Meta:
        model = SingInModel
        fields = ('password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'پسورد جدید'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'تکرار پسورد جدید'})
        }
        error_messages = {
            'password': {'required': 'پسورد اشتباه است'},
            'confirm_password': {'required': 'تکرار پسورد اشتباه است'},
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('پسورد با تکرار پسور مغایرت دارد')
