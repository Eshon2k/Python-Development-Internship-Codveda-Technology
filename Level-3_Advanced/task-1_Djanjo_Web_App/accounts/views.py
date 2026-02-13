from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # Add this import

@login_required # This line protects the view below
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Changed to redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
