from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, template_name='registration/signup.html', context={'form': form})
