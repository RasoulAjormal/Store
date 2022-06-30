from django.urls import path

from account_module.views import LogInAndSingIn, LoginView, SinginView, ActiveAccountCodeView, ForgetPasswordView, \
    ResetPasswordView, Logout

urlpatterns = [
    path('LogInAndSingIn/', LogInAndSingIn.as_view(), name='LogInAndSingInPageUrl'),
    path('LogIn/', LoginView.as_view(), name='LogInPageUrl'),
    path('Logout/', Logout.as_view(), name='LogoutPageUrl'),
    path('SingIn/', SinginView.as_view(), name='SingInPageUrl'),
    path('ActiveCode/<random_str_code>', ActiveAccountCodeView.as_view(), name='ActiveCodePageUrl'),
    path('RestPassword/<email_active_code>', ResetPasswordView.as_view(), name='ResetPasswordPageUrl'),
    path('ForgetPassword/', ForgetPasswordView.as_view(), name='ForgetPasswordPageUrl'),
]
