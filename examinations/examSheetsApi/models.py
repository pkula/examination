from django.db import models



class ExamSheet(models.Model):
    is_published = models.BooleanField(default=False)
    #questions = wiele questiionss
    # many to one superuser




class AnswerForm(models.Model):
    exam_sheet = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='answer_forms')
    #exam_sheet = foreign key   ExamSheet  # one to many
    #answers = //
    #total_mark   - its not a field there is a function

class Question(models.Model):
    question = models.TextField(max_length=100)
    max_mark = models.IntegerField(blank=True, null=True)
    sheet = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='questions')



class Answer(models.Model):
    answer = models.TextField(max_length=110)
    mark = models.IntegerField(blank=True, null=True) #superuser mark this field
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    form = models.ForeignKey(AnswerForm, on_delete=models.CASCADE, related_name='answers')


