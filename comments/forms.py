from django import forms
from .models import Comment, ForbiddenWord
import re

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
        FORBIDDEN_WORDS = ForbiddenWord.objects.values_list('word',flat=True)
        for word in FORBIDDEN_WORDS:
            content = re.sub(rf'\b{re.escape(word)}\b',
                                   '*' * len(word),
                                   content,flags=re.IGNORECASE)
        return content
    
    def clean(self):
        cleaned_content = super().clean()
        parent = cleaned_content.get("parent")
        if parent and parent.parent:
            raise forms.ValidationError("You cannot reply to a reply")
        return cleaned_content
