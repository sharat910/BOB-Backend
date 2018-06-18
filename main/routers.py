from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()

router.register(r'teacher', TeacherViewSet)
# router.register(r'parent', ParentViewSet)
router.register(r'student', StudentViewSet)
router.register(r'batch', BatchViewSet)
router.register(r'level', LevelViewSet)
router.register(r'month', MonthViewSet)
router.register(r'examresult', ExamResultViewSet)
router.register(r'feerecord', FeeRecordViewSet)
router.register(r'salaryrecord', SalaryRecordViewSet)
router.register(r'salaryrate', SalaryRateViewSet)
router.register(r'feerate', FeeRateViewSet)
router.register(r'royaltyrate', RoyaltyRateViewSet)
router.register(r'expenditure', ExpenditureViewSet)
