from django.db import models
from .choices import *
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.name), filename)

# Create your models here.

class Level(models.Model):
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.level

    @property
    def summary(self):
        return str(self)

class Month(models.Model):
    month = models.CharField(max_length=10, choices=MONTHS,default='None')

    def __str__(self):
        return self.month

    @property
    def summary(self):
        return str(self)

class Expenditure(models.Model):
    date = models.DateField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return "%d | %s" % (self.amount,self.description)

    @property
    def summary(self):
        return str(self)

class SalaryRate(models.Model):
    salary_rate = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.salary_rate)

    @property
    def summary(self):
        return str(self)

class FeeRate(models.Model):
    month_fee = models.IntegerField()
    level_fee = models.IntegerField()
    exam_fee = models.IntegerField()
    registration_fee = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.level_fee)

    @property
    def summary(self):
        return str(self)

class RoyaltyRate(models.Model):
    month_royalty = models.IntegerField()
    level_royalty = models.IntegerField()
    exam_royalty = models.IntegerField()
    registration_royalty = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.level_fee)

    @property
    def summary(self):
        return str(self)

class Centre(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.name)

    def summary(self):
        return str(self)

class Teacher(models.Model):
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    trained_max_level = models.ForeignKey(
        Level, models.SET_NULL, related_name='teachers', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def summary(self):
        return str(self)

    @property
    def trained_max_level_detail(self):
        return str(self.trained_max_level)

class Batch(models.Model):
    timing = models.CharField(max_length=10, choices=TIMING_CHOICES)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    level = models.ForeignKey(
        Level, models.SET_NULL, related_name='batches', blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, models.SET_NULL,related_name='batches', blank=True, null=True)
    centre = models.ForeignKey(
        Centre, models.SET_NULL,related_name='batches', blank=True, null=True)
    level_start_date = models.DateField()


    def __str__(self):
        return "%s | %s | %s | %s" % (self.day, self.timing, self.level.level, self.centre.name)


    @property
    def summary(self):
        return str(self)

    @property
    def level_detail(self):
        return str(self.level)

# class Parent(models.Model):
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     parent_type = models.CharField(max_length=6, choices=PARENT_TYPES)
#
#     def __str__(self):
#         return "%s | %s" % (self.parent_type, self.name)
#
#     @property
#     def summary(self):
#         return str(self)

class Student(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    batch = models.ForeignKey(Batch, models.SET_NULL, related_name='students',blank=True, null=True)

    date_of_birth = models.DateField(null=True,blank=True)
    date_of_joining = models.DateField(null=True,blank=True)
    # parents = models.ManyToManyField(Parent, related_name='students')
    #exam_results = models.ManyToManyField(ExamResult)

    #photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    #Parent_details
    father_name = models.CharField(max_length=200,null=True,blank=True)
    mother_name = models.CharField(max_length=200,null=True,blank=True)

    #Contact Details
    phone = models.CharField(max_length=13)
    alt_phone = models.CharField(max_length=13,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    performance_rating = models.CharField(max_length=6, null=True,blank=True,
                                choices=PERFORMANCE_CHOICES,default='Medium')
    dropped = models.BooleanField(default=False)
    date_dropped = models.DateField(blank=True,null=True)
    graduated = models.BooleanField(default=False)
    date_graduated = models.DateField(blank=True,null=True)
    t_shirt_size = models.CharField(max_length=4,blank=True,null=True, choices=T_SHIRT_SIZES)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def summary(self):
        return str(self)

class ExamResult(models.Model):
    student = models.ForeignKey(
        Student, models.SET_NULL, related_name='examresults', blank=True, null=True)
    level = models.ForeignKey(
        Level, models.SET_NULL, related_name='examresults', blank=True, null=True)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)
    date_of_exam = models.DateField()

    def __str__(self):
        return "%s | %s | %d/%d" % (self.student.name,self.level.level,self.score,self.max_score)

    @property
    def summary(self):
        return str(self)

class FeeRecord(models.Model):
    student = models.ForeignKey(
        Student, models.SET_NULL, related_name='feerecords', blank=True, null=True)
    fee_type = models.CharField(max_length=10, choices=FEE_TYPES)
    fee_amount = models.IntegerField()
    fee_receipt_no = models.IntegerField()
    level = models.ForeignKey(
        Level, models.SET_NULL, related_name='feerecords', blank=True, null=True)
    months = models.ManyToManyField(Month, related_name='feerecords')
    date_of_payment = models.DateField()
    balance = models.IntegerField()
    due = models.IntegerField()

    def __str__(self):
        if self.fee_type == 'Level':
            return "%s | %s fee | %s" % (self.student.name, self.fee_type, self.level.level)
        else:
            return "%s | %s fee | %s" % (self.student.name, self.fee_type, self.month.month)

    @property
    def summary(self):
        return str(self)

class SalaryRecord(models.Model):
    teacher = models.ForeignKey(
        Teacher, models.SET_NULL, related_name='salaryrecords', blank=True, null=True)
    salary_type = models.CharField(max_length=10, choices=SALARY_TYPES)
    salary_amount = models.IntegerField()
    months = models.ManyToManyField(Month, related_name='salaryrecords')
    level = models.ForeignKey(
        Level, models.SET_NULL, related_name='salaryrecords', blank=True, null=True)
    batch = models.ForeignKey(
        Batch, models.SET_NULL, related_name='salaryrecords', blank=True, null=True)
    date_of_payment = models.DateField()
    balance = models.IntegerField()
    due = models.IntegerField()

    def __str__(self):
        return "%s | %s" % (self.teacher.name,self.month.month)

    @property
    def summary(self):
        return str(self)
