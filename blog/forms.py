from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author","body", "categories")

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),  # or any other appropriate widget
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body","categories")

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),  # or any other appropriate widget

        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            
            'name': forms.TextInput(attrs={'class':'form-control'}),

        }