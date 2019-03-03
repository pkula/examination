from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
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
    UserSerializer
)
from django.contrib.auth.models import User


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
                        owner=request.user)
            serializer = QuestionSerializer(form, many=False)
            return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.max_score = request.data['max_score']
        instance.question_content = request.data['question_content']
        instance.save()

        serializer = QuestionSerializer(instance, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        form = Answer.objects.create(
            question_id=Question.objects.get(id=int(request.data['question_id'])),
            form_id=AnswerForm.objects.get(id=int(request.data['form_id'])),
            answer_content=request.data['answer_content'],
                    user=request.user)
        serializer = AnswerSerializer(form, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AnswerSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return Response("You can't change youre answer")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')


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
        queryset = self.get_queryset()

        serializer = ExamSheetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ExamSheetSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.title = request.data['title']
        instance.save()

        serializer = ExamSheetSerializer(instance, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')


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
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        form = AnswerForm.objects.create(
            exam_sheet_id=ExamSheet.objects.get(id=int(request.data['exam_sheet_id'])),
            user=request.user)
        serializer = AnswerFormSerializer(form, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = AnswerFormSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AnswerFormSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return Response("You can't update your answer")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')


















class MyOwnModelViewSet(viewsets.ModelViewSet):
    #queryset = MyOwnModel.objects.all()
    serializer_class = MyOwnModelSerializer
    authentication_classes = (TokenAuthentication, )

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
            my_model = MyOwnModel.objects.create(q=request.data["q"],
                        a=request.data["a"], user=request.user)
            serializer = MyOwnModelSerializer(my_model, many=False)
            return Response(serializer.data)



    '''def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.q = request.data['q']
        instance.a = request.data['a']
        instance.save()

        serializer = MyOwnModelSerializer(instance, many=False)
        return Response(serializer.data)'''

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        '''if  instance.user == request.user:
            instance.q = request.data['q']
            instance.a = request.data['a']
            instance.save()

            serializer = MyOwnModelSerializer(instance, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')
         '''   #return Response(ono)


        if  is_authorization(self, request):
            instance.q = request.data['q']
            instance.a = request.data['a']
            instance.save()

            serializer = MyOwnModelSerializer(instance, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')
            #return Response(ono)







    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Record deleted')



def is_authorization(self, request):
    instance = self.get_object()
    return instance.user == request.user