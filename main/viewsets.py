from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .paginations import LargePagination
from .models import *
from .serializers import *
#from .bobfunctions.monthly_statements import generate_monthly_statement
import json

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CentreViewSet(viewsets.ModelViewSet):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'code', 'batch_details')
    ordering = ('code',)

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    @action(detail=True)
    def generate_monthly_statement(self,request,pk):
        batch = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(batch)
        file_url = generate_monthly_statement(serializer.data)
        return Response({'url': file_url})

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

    @action(detail=False)
    def get_rate(self,request):
        rate = SalaryRate.objects.get(pk=1)
        serializer = SalaryRateSerializer(rate)
        return Response(serializer.data)

    @action(methods=['post'],detail=False)
    def set_rate(self,request):
        rate = SalaryRate.objects.get(pk=1)
        serializer = SalaryRateSerializer(rate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Rate set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class FeeRateViewSet(viewsets.ModelViewSet):
    queryset = FeeRate.objects.all()
    serializer_class = FeeRateSerializer

    @action(detail=False)
    def get_rate(self,request):
        rate = FeeRate.objects.get(pk=1)
        serializer = FeeRateSerializer(rate)
        return Response(serializer.data)

    @action(methods=['post'],detail=False)
    def set_rate(self,request):
        rate = FeeRate.objects.get(pk=1)
        serializer = FeeRateSerializer(rate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Rate set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class RoyaltyRateViewSet(viewsets.ModelViewSet):
    queryset = RoyaltyRate.objects.all()
    serializer_class = RoyaltyRateSerializer

    @action(detail=False)
    def get_rate(self,request):
        rate = RoyaltyRate.objects.get(pk=1)
        serializer = RoyaltyRateSerializer(rate)
        return Response(serializer.data)

    @action(methods=['post'],detail=False)
    def set_rate(self,request):
        rate = RoyaltyRate.objects.get(pk=1)
        serializer = RoyaltyRateSerializer(rate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Rate set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('voucher_id', 'description', 'date','amount')
    ordering = ('-date',)
    # pagination_class = LargePagination
