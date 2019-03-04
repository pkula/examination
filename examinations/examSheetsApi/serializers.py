from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
    Question, Answer, AnswerForm,
    ExamSheet,
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
        fields = ('id', 'sheet_id', 'max_score', 'owner', 'question_content')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_content', 'score', 'question_id', 'form_id')


class AnswerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerForm
        fields = ('id', 'exam_sheet_id', 'answers', 'mark')


class ExamSheetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    answer_forms = AnswerFormSerializer(many=True)
    class Meta:
        model = ExamSheet
        fields = ('id', 'title', 'owner', 'is_published', 'questions', 'answer_forms')


class UserExamSheetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = ExamSheet
        fields = ('id', 'title', 'questions')