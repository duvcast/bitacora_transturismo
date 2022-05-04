from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class LoginUserView(LoginView):
    template_name = 'main/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('administremos:novelties')
        return super(LoginUserView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'iniciar Sesion'
        return context



