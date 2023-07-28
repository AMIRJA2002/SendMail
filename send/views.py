from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import EmailForm
from django.views import View


class SendEmail(View):

    def get(self, request):
        form = EmailForm()
        return render(request, 'email_form.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_email = form.cleaned_data['sender_email']
            receiver_email = form.cleaned_data['receiver_email']
            image = form.cleaned_data['image']
            message = form.cleaned_data['message']

            email = EmailMessage(
                subject=subject,
                body=f'sender: {sender_email},\t message: {message}',
                from_email=sender_email,
                to=[receiver_email],
            )

            email.attach(image.name, image.read(), image.content_type)

            try:
                email.send()
                return render(request, 'success.html')
            except Exception as e:
                return render(request, 'error.html')
        else:
            form = EmailForm()
        return render(request, 'email_form.html', {'form': form})
