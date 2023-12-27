from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import RegisterForm


class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Hello {username}. Your account has created')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_auth/reset_password.html'
    email_template_name = 'app_auth/password_reset_email.html'
    html_email_template_name = 'app_auth/password_reset_email.html'
    success_url = reverse_lazy('app_auth:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'app_auth/password_reset_subject.txt'
