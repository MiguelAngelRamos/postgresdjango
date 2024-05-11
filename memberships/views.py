from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm
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

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'memberships/login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')