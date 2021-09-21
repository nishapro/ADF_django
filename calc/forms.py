from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import requestTable


class RequestForm(ModelForm):
    class Meta:
        model = requestTable
        fields = '__all__'
    def clean(self):
        super(RequestForm,self).clean()
        pin=self.cleaned_data.get('pincode')
        pan=self.cleaned_data.get('pan')
        if(str(pin))<6:
            self.errors['pin']=self.error_class(['minimum 6 digit is required for pin'])
        if len(pan)<10:
            self.errors['pan']=self.error_class(['PAN should contain 10 characters'])

        return self.cleaned_data








