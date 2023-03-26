from django import forms

class SurveyForm(forms.Form):
    title = forms.CharField(label='제목', max_length=255)
    description_prompt = forms.CharField(label='설문조사 내용', widget=forms.Textarea)
