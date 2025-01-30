from django import forms
from .models import Post  # Import the Post model (or another model you're using)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Replace with your Post model
        fields = ['title', 'content', 'image']  # Adjust the fields as per your model