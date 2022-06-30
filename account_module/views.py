from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from account_module.forms import SingInForm, LogInForm, ForgetPasswordForm, ResetPasswordForm
from account_module.models import User
from utils.email import send_email


# Create your views here.


class LogInAndSingIn(View):
    def get(self, request):
        register_form = SingInForm()
        login_form = LogInForm()
        return render(request, 'LogInAndSingIn.html', {'Register_form': register_form, 'LogIn_form': login_form})


class SinginView(View):
    def post(self, request):
        register_form = SingInForm(request.POST)
        login_form = LogInForm()
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')

            NewUser = User(
                username=username,
                is_active=False,
                email=email,
                email_active_code=get_random_string(72),
            )
            NewUser.set_password(password)
            NewUser.save()
            if send_email('فعالسازی حساب کاربری', NewUser.email, {'NewUser': NewUser},
                          'emails/Email_Activate_Account.html'):
                register_form.add_error('email', 'یک ایمیل حاوی کد فعالسازی برای شما ارسال شده است.')
            else:
                register_form.add_error('email', 'متاسفانه ایمیل ارسال نشد دوباره تلاش کنید.')
                NewUser.delete()

        return render(request, 'LogInAndSingIn.html', {'Register_form': register_form, 'LogIn_form': login_form})


class LoginView(View):
    def post(self, request):
        login_form = LogInForm(request.POST)
        register_form = SingInForm()
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(username__iexact=username).first()
            if user is not None:
                is_password_correct = user.check_password(password)
                if is_password_correct:
                    if not user.is_active:
                        login_form.add_error('username', 'نام کاربری شما فعال نمی باشد.')
                    else:
                        login(request, user)
                        return redirect(reverse('HomePageUrl'))
                else:
                    login_form.add_error('username', 'پسورد یا رمز عبور اشتباه می باشد')
            else:
                login_form.add_error('username', 'پسورد یا رمز عبور اشتباه می باشد')

        return render(request, 'LogInAndSingIn.html', {'Register_form': register_form, 'LogIn_form': login_form})


class ActiveAccountCodeView(View):
    def get(self, request, random_str_code):
        user: User = User.objects.filter(email_active_code__iexact=random_str_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('LogInAndSingInPageUrl'))
            else:
                pass
        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        login_form = LogInForm()
        forget_pass = ForgetPasswordForm()
        return render(request, 'ForgetPassword.html', {'login_form': login_form, 'forget_pass': forget_pass})

    def post(self, request):
        forget_pass = ForgetPasswordForm(request.POST)
        login_form = LogInForm()
        if forget_pass.is_valid():
            email = forget_pass.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if send_email('بازیابی پسورد حساب کاربری', user.email, {'user': user},
                              'emails/Email_Forget_Password.html'):
                    forget_pass.add_error('email', 'یک ایمیـل حاوی لینک بازیابی کلمـه عبـور برای شما ارسال خواهـد شد')
                else:
                    forget_pass.add_error('email', 'متاسفانه مشکلی به وجود آمد. دوباره تلاش کنید')
            else:
                forget_pass.add_error('email', 'ایمیل اشتباه می باشد.')
        else:
            forget_pass.add_error('email', 'ایمیل اشتباه می باشد.')
        return render(request, 'ForgetPassword.html', {'forget_pass': forget_pass, 'login_form': login_form})


class ResetPasswordView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is None:
            return redirect(reverse('ForgetPasswordPageUrl', ))
        reset_form = ResetPasswordForm()
        return render(request, 'Reset_Password.html', {'reset_form': reset_form, 'user': user})

    def post(self, request, email_active_code):
        reset_form = ResetPasswordForm(request.POST)
        if reset_form.is_valid():
            password = reset_form.cleaned_data.get('password')
            user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
            user.set_password(password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('HomePageUrl'))
        return render(request, 'Reset_Password.html', {'reset_form': reset_form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('LogInAndSingInPageUrl'))
