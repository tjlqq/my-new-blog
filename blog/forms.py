from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()