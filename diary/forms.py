from django import forms
from diary.models import Chapter, Comment


class ChapterForm(forms.ModelForm):

    class Meta():
        model = Chapter
        fields = ('author', 'title', 'text')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
    }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
