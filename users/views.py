from django.shortcuts import render, HttpResponse
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})