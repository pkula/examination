from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http.response import HttpResponseNotAllowed

from examinations.examSheetsApi.serializers import (
    UserSerializer, GroupSerializer,
)
from .models import (
    Question, Answer,
    ExamSheet, AnswerForm,
    MyOwnModel,
)
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    AnswerFormSerializer,
    ExamSheetSerializer,
    MyOwnModelSerializer,
)



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

    def get_queryset(self):
        questions = Question.objects.all()
        return questions

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        #page = self.paginate_queryset(queryset)
        #if page is not None:
        #    serializer = self.get_serializer(page, many=True)
        #    return self.get_paginated_response(serializer.data)

        serializer = QuestionMini(queryset, many=True)
        return Response(serializer.data)



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QuestionMini(instance)
        return Response(serializer.data)






class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ExamSheetViewSet(viewsets.ModelViewSet):
    queryset = ExamSheet.objects.all()
    serializer_class = ExamSheetSerializer

    @action(detail=True)
    def publish(self, request, **kwargs):
        exam = self.get_object()
        exam.is_published = True
        exam.save()

        serializer = ExamSheetSerializer(exam, many=False)
        return Response(serializer.data)

    @action(detail=True)
    def unpublish(self, request, **kwargs):
        exam = self.get_object()
        exam.is_published = False
        exam.save()

        serializer = ExamSheetSerializer(exam, many=False)
        return Response(serializer.data)


class AnswerFormViewSet(viewsets.ModelViewSet):
    queryset = AnswerForm.objects.all()
    serializer_class = AnswerFormSerializer



class MyOwnModelViewSet(viewsets.ModelViewSet):
    #queryset = MyOwnModel.objects.all()
    serializer_class = MyOwnModelSerializer

    def get_queryset(self):
        # in this place i can choose queryset
        #qs = MyOwnModel.objects.filter(id=2)
        qs = MyOwnModel.objects.all()
        return qs
    queryset = get_queryset(MyOwnModel)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = MyOwnModelSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MyOwnModelSerializer(instance)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            my_model = MyOwnModel.objects.create(q=request.data["q"], a=request.data["a"])
            serializer = MyOwnModelSerializer(my_model, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')


    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.q = request.data['q']
        instance.a = request.data['a']
        instance.save()

        serializer = MyOwnModelSerializer(instance, many=False)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')