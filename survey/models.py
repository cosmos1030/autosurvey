from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    CHECKBOX = 'checkbox'

    INPUT_TYPES = (
        (TEXT, '한 줄 입력'),
        (RADIO, '라디오 버튼'),
        (CHECKBOX, '체크박스'),
    )

    survey = models.ForeignKey('Survey', related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    input_type = models.CharField(max_length=20, choices=INPUT_TYPES)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
