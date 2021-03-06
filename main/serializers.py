from rest_framework import serializers
from .models import *

class CustomSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class CentreSerializer(CustomSerializer):
    class Meta:
        model = Centre
        fields = '__all__'
        extra_fields= ['summary']

class SalaryRecordSerializer(CustomSerializer):
    month_names = serializers.StringRelatedField(source='months',many=True,read_only=True)
    batch_details = serializers.StringRelatedField(source='batch',read_only=True)
    level_details = serializers.StringRelatedField(source='level',read_only=True)

    class Meta:
        model = SalaryRecord
        fields = '__all__'
        extra_fields= ['summary','month_names','batch_details','level_details']

class ExamResultSerializer(CustomSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
        extra_fields= ['summary']


class FeeRecordSerializer(CustomSerializer):
    month_names = serializers.StringRelatedField(source='months',many=True,read_only=True)
    class Meta:
        model = FeeRecord
        fields = '__all__'
        extra_fields= ['summary','month_names']


# class ParentSerializer(CustomSerializer):
#     class Meta:
#         model = Parent
#         fields = '__all__'
#         extra_fields= ['summary']


class StudentSerializer(CustomSerializer):
    batch_details = serializers.StringRelatedField(source='batch',read_only=True)
    # parent_details = ParentSerializer(source='parents',read_only=True,many=True)
    feerecords = FeeRecordSerializer(read_only=True,many=True)
    examresults = ExamResultSerializer(read_only=True,many=True)

    class Meta:
        model = Student
        fields = '__all__'
        extra_fields = ['feerecords','batch_details','examresults']#,'parent_details']

class BatchSerializer(CustomSerializer):
    #students = serializers.StringRelatedField(many=True)
    students = StudentSerializer(many=True, read_only=True)
    teacher_name = serializers.SlugRelatedField(source='teacher', read_only=True, slug_field='name')
    # centre_name = serializers.SlugRelatedField(source='centre', read_only=True, slug_field='name')
    # centre_area = serializers.SlugRelatedField(source='centre', read_only=True, slug_field='area')

    class Meta:
        model = Batch
        fields = '__all__'
        extra_fields= ['students','teacher_name','level_detail','summary']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['centre_exp'] = CentreSerializer(
            Centre.objects.get(pk=data['centre'])).data
        return data

class TeacherSerializer(CustomSerializer):
    batches = BatchSerializer(many=True,read_only=True)
    salaryrecords = SalaryRecordSerializer(read_only=True,many=True)

    class Meta:
        model = Teacher
        fields = '__all__'
        extra_fields = ['summary','batches','trained_max_level_detail','salaryrecords']

class LevelSerializer(CustomSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        extra_fields= ['summary']

class MonthSerializer(CustomSerializer):
    class Meta:
        model = Month
        fields = '__all__'
        extra_fields= ['summary']

class SalaryRateSerializer(CustomSerializer):
    class Meta:
        model = SalaryRate
        fields = '__all__'

class FeeRateSerializer(CustomSerializer):
    class Meta:
        model = FeeRate
        fields = '__all__'

class RoyaltyRateSerializer(CustomSerializer):
    class Meta:
        model = RoyaltyRate
        fields = '__all__'

class ExpenditureSerializer(CustomSerializer):
    class Meta:
        model = Expenditure
        fields = '__all__'
