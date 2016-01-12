from django.shortcuts import render
from django.http import HttpResponseRedirect
from info.form import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
import shutil
import os.path
def thanks(request):
    return HttpResponse("Thank you")
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['Source']
            destination = form.cleaned_data['Destination']
            email = form.cleaned_data['email']
            print source
            print destination
            print email
            if os.path.exists(source):
             shutil.copy(source,destination)
             send_mail('Alert', 'File copied successfully', 'anerishah3110@gmail.com', [email])
            else:
                send_mail('Alert', 'Unsuccessful', 'anerishah3110@gmail.com', [email])


            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
