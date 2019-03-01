from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from examinations.examSheetsApi.serializers import UserSerializer, GroupSerializer
from .models import Question
from .serializers import QuestionSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    get_queryset(self):

