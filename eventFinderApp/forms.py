from django.forms import ModelForm, SplitDateTimeField, ValidationError
from .models import Event, Category, Account
from django.contrib.admin import widgets
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ['host']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time > end_time:
            raise ValidationError('Start time and date must be before end time and date.')
        
    def clean_content(self):    
        content = self.cleaned_data['content']
        content_type = content.content_type.split('/')[0]
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        else:
            raise ValidationError(_('File type is not supported'))
        return content




class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]