from django import forms

class PostForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    category = forms.CharField(label='Category', max_length=100)
    post = forms.CharField(label='Post Content', max_length=100)
