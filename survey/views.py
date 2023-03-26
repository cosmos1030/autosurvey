from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey
from .forms import SurveyForm
import openai

openai.api_key = "##"

def generate_survey(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text


def survey_create(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description_prompt = form.cleaned_data['description_prompt']
            description = generate_survey(description_prompt)
            survey = Survey(title=title, description=description)
            survey.save()
            return redirect('survey_detail', survey.pk)
    else:
        form = SurveyForm()
    return render(request, 'survey/survey_create.html', {'form': form})

def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.all()
    context = {'survey': survey, 'questions': questions}
    return render(request, 'survey/survey_detail.html', context)

