from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Question, Answer, AnswerForm, ExamSheet

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
        fields = ('id',)













class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', )

class ExamSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSheet
        fields = ('id', )

class AnswerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerForm
        fields = ('id', )