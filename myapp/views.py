from django.shortcuts import render
from django.views import View
from .forms import CusomUserChangeForm, CustomUserCreationForm


class UserRegister(View):
    def get(self, request, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'myapp/signup.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            return render(request, 'myapp/signup.html', {'form': form})