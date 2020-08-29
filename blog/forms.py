from django import forms
from .models import Post
from .models import CV

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name', 'address', 'email', 'mobile', 'linkedin', 'bio', 'employment', 'qualifications', 'experience', 'achievments', 'education', 'references')