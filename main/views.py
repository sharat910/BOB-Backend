from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class StudentEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_edit.html'

    def get(self, request, pk):
        print("Here")
        student = get_object_or_404(Student, pk=pk)
        print(student)
        serializer = StudentSerializer(student)
        print(serializer)
        return Response({'serializer': serializer, 'student': student})

    def post(self, request, pk):
        print("In post")
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if not serializer.is_valid():
            print("Serializer invalid")
            return Response({'serializer': serializer, 'student': student})
        serializer.save()
        print("After Save")
        return redirect('student-list')

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#def dashboard(request):

def add_new_student(request):
    f = StudentForm()    
    return render(request, 'student_form.html', {'form': f})

def add_new_student_rest(request):
    f = StudentForm()    
    return render(request, 'student_form.html', {'form': f})


