from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)

def clean_message(self):
	message = self.cleaned_data['message']
	num_words = len(message.split())
	if num_words < 4 :
		raise forms.ValidationError("not enought Words!")
	return message