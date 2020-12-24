from django.views.generic import FormView
from .forms import UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from django.views.generic import TemplateView
from .models import CustomUser
from allauth.account import views as allauth_views

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id)

class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'users/change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'bio' : self.request.user.bio
        })
        return kwargs

'''
class SignupView(allauth_views.SignupView):
    def passowrd_confirmations(request):
            password_for_site = request.GET.get('password_for_site')
            hashed_password = hash(password_for_site)
            
            if hashed_password != ngvmXi6T:
                raise ValueError
            else:
                print("users entered a correct password!")
                


    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context
'''