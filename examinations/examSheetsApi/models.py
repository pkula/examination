from django.db import models
from django.contrib.auth.models import User


class ExamSheet(models.Model):
    title = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)

    superuser = models.ForeignKey(User, on_delete=models.CASCADE)



class AnswerForm(models.Model):
    exam_sheet_id = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='answer_forms')
    mark = models.IntegerField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    question_content = models.TextField(max_length=100, null=True, blank=True)
    max_score = models.IntegerField(blank=True, null=True)
    sheet_id = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='questions', )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    answer_content = models.TextField(max_length=110)
    score = models.IntegerField(blank=True, null=True) #superuser mark this field
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True,)
    form_id = models.ForeignKey(AnswerForm, on_delete=models.CASCADE, related_name='answers')

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MyOwnModel(models.Model):
    q = models.IntegerField()
    a = models.TextField(max_length=110)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
