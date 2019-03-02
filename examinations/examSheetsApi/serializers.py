from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Question, Answer, AnswerForm, ExamSheet, MyOwnModel



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
        fields = ('id', 'question')


class QuestionMini(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')
        read_only_fields = ('id',)

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=False)
    class Meta:
        model = Answer
        fields = ('id', 'mark', 'question')



class AnswerFormSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = AnswerForm
        fields = ('id', 'answers')


class ExamSheetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    answer_forms = AnswerFormSerializer(many=True)
    class Meta:
        model = ExamSheet
        fields = ('id', 'answer_forms', 'questions')
        #depth = 1




class MyOwnModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyOwnModel
        fields = ('id', 'q')
        #read_only_fields = ('id',)
        #depth = 1