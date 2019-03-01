from django.db import models

class Question(models.Model):
    question = models.TextField(max_length=100, default="it's not allowed")
    max_mark = models.IntegerField(blank=True)
    # many to one exam Sheet

class Answer(models.Model):
    answer = models.TextField(max_length=110)
    mark = models.IntegerField() #superuser mark this field
    #many to one AnswerForm

class ExamSheet(models.Model):
    is_published = models.BooleanField(default=False)
    #questions = wiele questiionss
    # many to one superuser

class AnswerForm(models.Model):
    pass
    #exam_sheet = foreign key   ExamSheet  # one to many
    #answers = //
    #total_mark   - its not a field there is a function
    # many to one user not creator
    # many to one superuser
