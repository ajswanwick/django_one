from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import League, Team, Goal_Profile, Post, Comment
from .forms import  PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
            return redirect(reverse('user_profile', kwargs={'username': user.username}))
        return self.render_to_response({'form': form, 'show_navbar': False})  # Re-render with errors
    
    def dispatch(self, request, *args, **kwargs):
        # If the user is already logged in, redirect to the profile page
        if request.user.is_authenticated:
            return redirect('user_profile', username=request.user.username)
        return super().dispatch(request, *args, **kwargs)

@login_required
def user_profile(request, username=None):
    user = get_object_or_404(User, username=username) if username else request.user
    posts = Post.objects.filter(user=user).order_by('-created_at')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = PostForm()

    return render(request, 'my_app/user_profile.html', {'user': user, 'posts': posts, 'form': form, 'show_navbar': True})


@login_required
def custom_login_redirect(request):
    """Redirect logged-in user to their profile page."""
    return redirect(reverse('user_profile', kwargs={'username': request.user.username}))



