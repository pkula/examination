from django.urls import include, path
from rest_framework import routers
from examinations.examSheetsApi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.QuestionViewSet)
router.register(r'exam_sheets', views.QuestionViewSet)
router.register(r'answer_form', views.QuestionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
