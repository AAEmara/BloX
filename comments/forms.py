from django import forms
from .models import Comment

FORBIDDEN_WORDS = ['fuck','shit','damn']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','parent']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['parent'].widget = forms.HiddenInput()
        self.fields['parent'].required = False
    
    def clean_content(self):
        content = self.cleaned_data.get('content','')
        for word in FORBIDDEN_WORDS:
            content = content.replace(word,'*' * len(word))
        return content
    
    def clean(self):
        cleaned_content = super().clean()
        parent = cleaned_content.get("parent")
        if parent and parent.parent:
            raise forms.ValidationError("You cannot reply to a reply")
        return cleaned_content
