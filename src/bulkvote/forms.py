from django import forms
from .models import Choice


class CreateVoteForm(forms.Form):
    description = forms.CharField(max_length=20, help_text='A description for this vote')
    author = forms.CharField(max_length=50, help_text='Your name')
    items = forms.CharField(help_text='List of items to vote on (one per line)', widget=forms.Textarea)
    choices = forms.CharField(help_text='List of choices for each item (one per line, first is default choice)', widget=forms.Textarea, initial='yes\nno')

    def clean(self):
        cleaned_data = super(CreateVoteForm, self).clean()
        
        if cleaned_data['description'] == '':
            self._errors['description'] = self.error_class(['Please enter a description for this vote'])
            del cleaned_data['description']

        if cleaned_data['items'] == '':
            self._errors['items'] = self.error_class(['Please enter at least one item to vote on (one per line)'])
            del cleaned_data['items']

        if len(cleaned_data['choices'].split('\n')) < 2:
            self._errors['choices'] = self.error_class(['Please enter at least two choices (one per line, first is default)'])
            del cleaned_data['choices']

        return cleaned_data


class ChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.vote = kwargs.pop('vote')
        super(ChoiceForm, self).__init__(*args, **kwargs)
        for item in self.vote.items.all():
            self.fields['choice_for_item_%s' % item.id] = forms.ModelChoiceField(
                widget=forms.RadioSelect, 
                queryset=Choice.objects.filter(vote=self.vote).order_by('id'), 
                initial=item.vote.choices.all()[0].id, # first choice is default 
                label=item.item
            )

    def clean(self):
        cleaned_data = super(ChoiceForm, self).clean()
        for item in self.vote.items.all():
            fieldname = 'choice_for_item_%s' % item.id
            choice = cleaned_data[fieldname]
            if choice not in Choice.objects.filter(vote=self.vote):
                self._errors[fieldname] = self.error_class(['Invalid choice for this item'])
                del cleaned_data[fieldname]
            return cleaned_data

