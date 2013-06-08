# encoding: utf-8

from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(label=u'Nome')
    email   = forms.EmailField(label=u'Email')
    message = forms.CharField(label=u'Mensagem', widget=forms.Textarea)