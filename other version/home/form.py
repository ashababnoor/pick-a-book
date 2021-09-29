from django import forms
try:
    from froala_editor.widgets import FroalaEditor
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'django-froala-editor'])
    from froala_editor.widgets import FroalaEditor


from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']
        
    