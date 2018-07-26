from datetime import datetime

def exam_this_month(batch_running_months):
    current_month =  datetime.today().month
    if current_month == batch_running_months[-1]:
        return True
    else:
        return False
