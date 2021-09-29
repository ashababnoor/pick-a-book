from django import forms

class ExchangeForm(forms.Form):
    title = forms.CharField(label='Tilte:',max_length=250)
    author = forms.CharField(label='Author name:',max_length=250)
    purchase_date = forms.DateField(label='Purchase date:')
    description = forms.CharField(label='Description:')
    edition = forms.DecimalField(label='Edition:',required=False)
    publisher = forms.CharField(label='Publisher:',required=False)
    prefered_books = forms.CharField(label='List your preferences:')
    #need to add image field in html form
    #< input type = "image" name = "images" multiple >