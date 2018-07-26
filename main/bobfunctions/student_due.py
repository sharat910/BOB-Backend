from django.shortcuts import get_object_or_404
from datetime import date,datetime
from main.models import Student

def fetch_current_level_feerecords(student):
    return filter(lambda feerecord: feerecord.level == student.batch.level, student.feerecords.all())

def get_running_months(batch):
    batch_running_months = [month.id for month in batch.running_months.all()]
    return batch_running_months

def get_student_dues(student_id):
    due_dict = {'due': True,
                'first_month':'NP',
                'second_month': 'NP',
                'third_month': 'NP',
                'exam': 'NP'}
    student = get_object_or_404(Student,pk=student_id)

    if student.dropped or student.graduated:
        due_dict['due'] = False
        return due_dict


    running_months = get_running_months(student.batch)
    current_month = datetime.today().month
    feerecords = fetch_current_level_feerecords(student)

    for feerecord in feerecords:
        if feerecord.fee_type == 'Level':
            due_dict['first_month'] = 'P'
            due_dict['second_month'] = 'P'
            due_dict['third_month'] = 'P'
        elif feerecord.fee_type == 'Exam':
            due_dict['exam'] = 'P'
        elif feerecord.fee_type == 'Month':
            month_paid_for = feerecord.months.all()[0].id
            if month_paid_for not in running_months:
                print( "Error")
            idx = running_months.index(month_paid_for)
            if idx == 0:
                due_dict['first_month'] = 'P'
            elif idx == 1:
                due_dict['second_month'] = 'P'
            elif idx == 2:
                due_dict['third_month'] = 'P'

    curr_idx = running_months.index(current_month)
    if curr_idx == 0:
        if due_dict['first_month'] == 'P':
            due_dict['due'] = False
        else:
            due_dict['due'] = True
    elif curr_idx == 1:
        if due_dict['first_month'] == 'P' and due_dict['second_month'] == 'P':
            due_dict['due'] = False
        else:
            due_dict['due'] = True
    elif curr_idx == 2:
        if due_dict['first_month'] == 'P' and due_dict['second_month'] == 'P'\
        and due_dict['third_month'] == 'P' and due_dict['exam'] == 'P':
            due_dict['due'] = False
        else:
            due_dict['due'] = True

    return due_dict

if __name__ == '__main__':
    get_student_dues(2,'2018-07-21')
