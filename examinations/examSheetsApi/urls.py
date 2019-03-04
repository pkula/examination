from django.urls import include, path
from rest_framework import routers
from examinations.examSheetsApi import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'exam_sheets', views.ExamSheetViewSet)
router.register(r'answer_forms', views.AnswerFormViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

