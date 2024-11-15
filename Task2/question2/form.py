from django.forms import ModelForm

from .models import Employee

class EmployeeForm(ModelForm):

    class Meta:
         model=Employee
         fields=['name','description','start_date','end_date']

    def clean(self):
         
        start_date=self.cleaned_data.get('start_date')
        end_date=self.cleaned_data.get('end_date')


        if start_date>end_date:
            raise ValueError('start date must be before end date')

        return self.cleaned_data




