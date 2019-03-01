from django.db import models

class Question(models.Model):
    question = models.TextField(max_length=100, default="it's not allowed")
    max_mark = models.IntegerField()

class Answer(models.Model):
    answer = models.TextField(max_length=110)
    mark = models.IntegerField()

class ExamSheet(models.Model):
    questions = wiele questiionss

class AnswerForm(models.Model):
    exam_sheet = foreign key   ExamSheet  # one to many
    answers = //
    total_mark =   # superuser mark this answers