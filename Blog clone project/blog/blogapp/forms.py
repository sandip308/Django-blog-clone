from django import forms
from .models import Post,Comment

class Postform(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text') # Grab from Model
        widget = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent',
                                            'placeholder':"Type Your Text Here"}) # editable medium-editor-textarea default class which is from medium-editor github, postcontent own created class
        }

class Commentform(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')
        widget = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
             'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea',
                                             'placeholder':"Type your text here"})
        }