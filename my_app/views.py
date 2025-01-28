from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.



class HomePage(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm()  # Add the login form to the context
        context['show_navbar'] = False # Hide the navbar
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to the homepage or another page
        return self.render_to_response({'form': form, 'show_navbar': False})  # Re-render with errors
      