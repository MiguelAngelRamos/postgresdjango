from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("is_valid")
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'memberships/register.html', {'form': form })