#encoding: utf-8

from django.shortcuts import render
from datetime import date
from forms import ContactForm

def home(request):
    context = {'nome' :u'Frederico', 'email':u'fredsilva.sistemas@gmail.com', 'data': date.today()}
    return render(request, 'home.html', context)

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['sucess'] = True
            #context['data'] = form.cleaned_data
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)