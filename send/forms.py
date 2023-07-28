from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(label='عنوان ایمیل', max_length=300)
    sender_email = forms.EmailField(label='آدرس ایمیل فرستنده')
    receiver_email = forms.EmailField(label='آدرس ایمیل گیرنده')
    image = forms.ImageField(label='تصویر')
    message = forms.CharField(label='توضیحات', widget=forms.Textarea)
