from django import forms
from Webapp.models import Question,Score2,Contact,Feedback,QuestionAns,Max,Sub,Time

 
class TimeForm(forms.ModelForm):
    class Meta:
        model=Time
        fields="__all__"

class SubForm(forms.ModelForm):
    class Meta:
        model=Sub
        fields="__all__"
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"

class QuestionAnsForm(forms.ModelForm):
    class Meta:
        model=QuestionAns
        fields="__all__"


class ScoreForm(forms.ModelForm):
    class Meta:
        model=Score2
        fields="__all__"

class MaxForm(forms.ModelForm):
    class Meta:
        model=Max
        fields="__all__"
