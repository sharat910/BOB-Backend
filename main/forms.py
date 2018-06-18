from .models import *
from django.forms import ModelForm

class BootStrapModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BootStrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = "__all__"