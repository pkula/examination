from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

from django.http.response import HttpResponseNotAllowed

from examinations.examSheetsApi.serializers import (
    UserSerializer, GroupSerializer,
)
from .models import (
    Question, Answer,
    ExamSheet, AnswerForm,
)
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    AnswerFormSerializer,
    ExamSheetSerializer,
    UserExamSheetSerializer,
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
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        questions = Question.objects.all()
        return questions

    def create(self, request, *args, **kwargs):
        form = Question.objects.create(
            sheet_id=ExamSheet.objects.get(id=int(request.data['sheet_id'])),
            question_content=request.data['question_content'],
            max_score=request.data['max_score'],
            owner=request.user, )
        serializer = QuestionSerializer(form, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response("Choose exam_sheet")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:
            instance.max_score = request.data['max_score']
            instance.question_content = request.data['question_content']
            instance.save()
            serializer = QuestionSerializer(instance, many=False)
            return Response(serializer.data)
        else:
            Response("You're not allowed")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:
            instance = self.get_object()
            instance.delete()
            return Response('Record deleted')
        else:
            Response("You're not allowed")

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        form = Answer.objects.create(
            question_id=Question.objects.get(id=int(request.data['question_id'])),
            form_id=AnswerForm.objects.get(id=int(request.data['form_id'])),
            answer_content=request.data['answer_content'],
            user=request.user, )
        serializer = AnswerSerializer(form, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response("Choose your answer sheet")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        question = self.get_object().question_id
        if question.owner == request.user or instance.user == request.user:
            serializer = AnswerSerializer(instance)
            return Response(serializer.data)
        else:
            Response("You're not allowed")

    def update(self, request, *args, **kwargs):
        return Response("You can't change youre answer")

    def destroy(self, request, *args, **kwargs):
        question = self.get_object().question_id
        if question.owner == request.user:
            instance = self.get_object()
            instance.delete()
            return Response('Record deleted')
        else:
            Response("You're not allowed")

    @action(detail=True,  methods=['post'])
    def mark(self, request, **kwargs):
        ans = self.get_object()
        question = self.get_object().question_id
        if question.owner == request.user:
            ans = self.get_object()
            ans.score = request.data['score']
            ans.save()

            serializer = AnswerSerializer(ans, many=False)
            return Response(serializer.data)
        else:
            Response("Not allow")


class ExamSheetViewSet(viewsets.ModelViewSet):
    queryset = ExamSheet.objects.all()
    serializer_class = ExamSheetSerializer
    authentication_classes = (TokenAuthentication,)


    def create(self, request, *args, **kwargs):
        exam = ExamSheet.objects.create(
            is_published=False,
            title=request.data['title'],
            owner=request.user)
        serializer = ExamSheetSerializer(exam, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = ExamSheet.objects.all()
        title = self.request.query_params.get('title', None)
        if title:
            queryset_title = ExamSheet.objects.filter(title__contains=title)
            serializer = UserExamSheetSerializer(queryset_title, many=True)
            return Response(serializer.data)
        else:
            serializer = UserExamSheetSerializer(queryset, many=True)
            return Response(serializer.data)



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:
            serializer = ExamSheetSerializer(instance)
            return Response(serializer.data)
        else:
            serializer = UserExamSheetSerializer(instance)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:
            instance.title = request.data['title']
            instance.save()
            serializer = ExamSheetSerializer(instance, many=False)
            return Response(serializer.data)
        else:
            Response("You're not allowed")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:
            instance = self.get_object()
            instance.delete()
            return Response('Record deleted')
        else:
            Response("You're not allowed")

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

    @action(detail=False)
    def my(self, request, **kwargs):
        user = request.user
        exams = ExamSheet.objects.filter(owner=user)

        serializer = ExamSheetSerializer(exams, many=True)
        return Response(serializer.data)


class AnswerFormViewSet(viewsets.ModelViewSet):
    queryset = AnswerForm.objects.all()
    serializer_class = AnswerFormSerializer
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        form = AnswerForm.objects.create(
            exam_sheet_id=ExamSheet.objects.get(id=int(request.data['exam_sheet_id'])),
            user=request.user)
        serializer = AnswerFormSerializer(form, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response("You are not allowed")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        exam = self.get_object().exam_sheet_id
        if exam.owner == request.user:
            serializer = AnswerFormSerializer(instance)
            return Response(serializer.data)
        else:
            Response("You're not allowed")

    def update(self, request, *args, **kwargs):
        return Response("You can't update your answer")

    def destroy(self, request, *args, **kwargs):
        exam = self.get_object().exam_sheet_id
        if exam.owner == request.user:
            instance = self.get_object()
            instance.delete()
            return Response('Record deleted')
        else:
            Response("You're not allowed")

    @action(detail=True,  methods=['post'])
    def mark(self, request, **kwargs):
        exam = self.get_object().exam_sheet_id
        if exam.owner == request.user:
            ans = self.get_object()
            ans.mark = request.data['mark']
            ans.save()

            serializer = AnswerFormSerializer(ans, many=False)
            return Response(serializer.data)
        else:
            Response("Not allow")

    @action(detail=False)
    def my(self, request, **kwargs):
        user = request.user
        forms = AnswerForm.objects.filter(user=user)

        serializer = AnswerFormSerializer(forms, many=True)
        return Response(serializer.data)

#def is_authorization(self, request, ):
#    instance = self.get_object()
#    return instance.user == request.user