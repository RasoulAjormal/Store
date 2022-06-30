from django import forms

from contact_module.models import ContactUsModel, SendNewsModel


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['fullname', 'title', 'email', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'id': 'message', 'placeholder': 'پیغام'})
        }
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'عنوان',
            'message': 'پیغام',
        }
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اچباری میباشد.لطفا وارد کنید'
            }
        }


class SendNewsForm(forms.ModelForm):
    class Meta:
        model = SendNewsModel
        fields = ('email',)
        widgets = {'email': forms.TextInput(
            attrs={'placeholder': 'آدرس ایمیل شما...'})}

    error_messages = {
        'email': {
            'required': 'ایمیل وارد شده اشتباه می باشد.'
        }
    }
