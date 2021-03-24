from django.shortcuts import redirect, render
from django.contrib import messages
from .form import CreateUser


def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'The user {user} is created :)')
            return redirect('login')
    else:
        form = CreateUser()

    data = {
        'form': form
    }
    return render(request, 'registration/signup.html', data)
