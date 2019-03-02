from django.db import models



class ExamSheet(models.Model):
    is_published = models.BooleanField(default=False)





class AnswerForm(models.Model):
    exam_sheet = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='answer_forms', default=1)
    #total_mark   - its not a field there is a function

class Question(models.Model):
    question = models.TextField(max_length=100, null=True, blank=True)
    max_mark = models.IntegerField(blank=True, null=True)
    #sheet = models.ForeignKey(ExamSheet, on_delete=models.CASCADE, related_name='questions', blank=True, null=True, default=1)



class Answer(models.Model):
    answer = models.TextField(max_length=110)
    mark = models.IntegerField(blank=True, null=True) #superuser mark this field
    #question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, default=1)
    #form = models.ForeignKey(AnswerForm, on_delete=models.CASCADE, related_name='answers', default=1)


class MyOwnModel(models.Model):
    q = models.TextField(max_length=110)
    a = models.TextField(max_length=110)