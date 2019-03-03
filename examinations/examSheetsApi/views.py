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


    '''def create(self, request, *args, **kwargs):
        question = MyOwnModel.objects.create(
            #question_content=request.data["question_content"],
            max_score=request.data["max_score"],
            #sheet_id=request.data["sheet_id"],
            #owner=request.user.id,
            #question_content="gsdaghsdghgds",
            #max_score=1,
            sheet_id=1,
            owner=1,)
        serializer = QuestionSerializer(my_model, many=False)
        return Response(serializer.data)
    '''



    def create(self, request, *args, **kwargs):
        my_dict = request.data
        my_dict = dict(my_dict)
        my_dict['owner'] = request.user.pk

        for key in my_dict:
            if key == 'question_content':
                my_dict[key] = my_dict[key][0]
            if key == 'max_score':
                try:
                    my_dict[key] = int(my_dict[key][0])
                except:
                    my_dict[key] = my_dict[key][0]
            if key == 'sheet_id':
                try:
                    my_dict[key] = int(my_dict[key][0])
                except:
                    my_dict[key] = my_dict[key][0]


        serializer = self.get_serializer(data=my_dict, )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)














    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AnswerSerializer(instance)
        return Response(serializer.data)


class ExamSheetViewSet(viewsets.ModelViewSet):
    queryset = ExamSheet.objects.all()
    serializer_class = ExamSheetSerializer
    authentication_classes = (TokenAuthentication,)

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


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = ExamSheetSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ExamSheetSerializer(instance)
        return Response(serializer.data)


class AnswerFormViewSet(viewsets.ModelViewSet):
    queryset = AnswerForm.objects.all()
    serializer_class = AnswerFormSerializer
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = AnswerFormSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AnswerFormSerializer(instance)
        return Response(serializer.data)


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


    '''def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            my_model = MyOwnModel.objects.create(q=request.data["q"], a=request.data["a"])
            serializer = MyOwnModelSerializer(my_model, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')
    '''

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