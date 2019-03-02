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
        fields = ('question',)


class QuestionMini(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')
        read_only_fields = ('id',)

class AnswerSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(many=False)
    class Meta:
        model = Answer
        fields = ('id', 'mark',)



class AnswerFormSerializer(serializers.ModelSerializer):
    #answers = AnswerSerializer(many=True)
    class Meta:
        model = AnswerForm
        fields = ('id', )


class ExamSheetSerializer(serializers.ModelSerializer):
    #questions = QuestionSerializer(many=True)
    #answer_forms = AnswerFormSerializer(many=True)
    class Meta:
        model = ExamSheet
        fields = ('id',)
        #depth = 1




class MyOwnModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyOwnModel
        fields = ('id', 'q','a')
        #read_only_fields = ('a',)
        #depth = 1