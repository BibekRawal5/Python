from django import forms

class ImageForm(forms.Form):
	name = forms.CharField()
	img_field = forms.ImageField()
