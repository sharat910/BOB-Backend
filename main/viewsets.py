from rest_framework import viewsets
from .models import *
from .serializers import *

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# class ParentViewSet(viewsets.ModelViewSet):
#     queryset = Parent.objects.all()
#     serializer_class = ParentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class FeeRecordViewSet(viewsets.ModelViewSet):
    queryset = FeeRecord.objects.all()
    serializer_class = FeeRecordSerializer

class SalaryRecordViewSet(viewsets.ModelViewSet):
    queryset = SalaryRecord.objects.all()
    serializer_class = SalaryRecordSerializer

class SalaryRateViewSet(viewsets.ModelViewSet):
    queryset = SalaryRate.objects.all()
    serializer_class = SalaryRateSerializer

class FeeRateViewSet(viewsets.ModelViewSet):
    queryset = FeeRate.objects.all()
    serializer_class = FeeRateSerializer

class RoyaltyRateViewSet(viewsets.ModelViewSet):
    queryset = RoyaltyRate.objects.all()
    serializer_class = RoyaltyRateSerializer

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
