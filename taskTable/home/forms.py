from django import forms
from .models import Task
# creating a form
class TaskForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError('Task name already exist')

        return title

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        start_date = self.cleaned_data['start_date']
        diff = (end_date-start_date).total_seconds()

        if diff<=0:
            raise forms.ValidationError('Incorrect end date')
        elif diff<1:
            raise forms.ValidationError('Minimum 1hr required for a task')
        return end_date

    class Meta:
        model = Task
        fields = ['title','start_date','end_date','priority']
        widgets = {
            'start_date':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_date':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
