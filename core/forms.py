# encoding: utf-8

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage

class ContactForm(forms.Form):
    name    = forms.CharField(label=u'Nome')
    email   = forms.EmailField(label=u'Email')
    message = forms.CharField(label=u'Mensagem', widget=forms.Textarea)

    def send_mail(self):
        subject = u'E-mail de Contato de %s' % self.cleaned_data['name']
        context = {'name':self.cleaned_data['name'], 'email': self.cleaned_data['email'], 'message': self.cleaned_data['message']}
        #message = u'E-mail: %s\nMensagem: %s' % (self.cleaned_data['email'], self.cleaned_data['message'])
        message = render_to_string('contact_mail.txt')
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMessage(subject, message_html, 'fredsilva.sistemas@gmail.com', ['fredsilva.sistemas@gmail.com'])
        #send_mail(subject, message, 'fredsilva.sistemas@gmail.com', ['fredsilva.sistemas@gmail.com'])
        msg.content_subtype = 'html'
        msg.send()