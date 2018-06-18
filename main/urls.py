from django.urls import path, include
from .routers import router
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path(r'api/', include(router.urls)),
    #path(r'students/', TemplateView.as_view(template_name='students.html'),name='student-list'),
    #path(r'student/new', views.add_new_student, name='new-student'),
    #path(r'student/edit/<int:pk>/', views.StudentEdit.as_view(), name='student-edit'),
]
