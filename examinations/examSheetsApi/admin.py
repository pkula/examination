from django.contrib import admin
from .models import Question, Answer, ExamSheet, AnswerForm, MyOwnModel

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ExamSheet)
admin.site.register(AnswerForm)
admin.site.register(MyOwnModel)