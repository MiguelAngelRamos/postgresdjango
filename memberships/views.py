from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # generamos una contraseña aleatoria
            temp_password = get_random_string(8)
            user.set_password(temp_password)
            user.save()
            # Enviar el correo electronico
            send_mail(
                'Tu contraseña Temporal - FitZone',
                f'Hola {user.first_name}, aqui está tu contraseña temporal: {temp_password}\n Por favor cambia esta contraseña tras iniciar sesión por primera vez',
                'tucorreo@outlook.com',
                [user.email],
                fail_silently = False
                
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'memberships/register.html', {'form': form })

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'memberships/login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')