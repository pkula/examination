from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
    Question, Answer, AnswerForm,
    ExamSheet, MyOwnModel,
)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_content', 'sheet_id', 'max_mark')


class AnswerSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    class Meta:
        model = Answer
        fields = ('id', 'answer_content', 'mark', 'question_id', 'form_id')



class AnswerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerForm
        fields = ('id', 'exam_sheet_id', 'answers')


class ExamSheetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    answer_forms = AnswerFormSerializer(many=True)
    class Meta:
        model = ExamSheet
        fields = ('id', 'is_published', 'questions', 'answer_forms')
        #depth = 1


class MyOwnModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyOwnModel
        fields = ('id', 'q','a')
        #read_only_fields = ('a',)
        #depth = 1
