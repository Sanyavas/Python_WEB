from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm


# def signupuser(request):
#     if request.user.is_authenticated:
#         return redirect(to='quotes:main')
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='quotes:main')
#         else:
#             return render(request, 'users/signup.html', context={'form': form})
#     return render(request, 'users/signup.html', context={'form': RegisterForm()})


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(to='quotes:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Hello {username}! Your account has been created.")
            return redirect(to="users:login")
        return render(request, self.template_name, {'form': form})
