from email.mime import text
from landingpage.forms import ContactForm
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView,ListView
from landingpage.models import Contact, ContactAndOTP
from django.http import request,response
from django.urls import reverse_lazy
import requests
from landingpage.send_mail import*
import string
import random

# Create your views here.
class LandingPageView(CreateView):
    model                               = Contact
    template_name                       = "index.html"
    form_class                          = ContactForm
    success_url                         = '/'
    success_message                     = 'Your Enquiry has been successfully submitted, You will be contacted soon'

    def post(self,request,*args, **kwargs):
        self.object                     = None
        form                            = self.get_form()
        # print(form.is_valid())
        if form.is_valid():
            if request.POST.get('otp') !=str(ContactAndOTP.objects.last().otp):
                return self.form_invalid(form)
            receipent                 ='XXXXXXXXXXXXXXXXXXXXx'
     
            to_emails                   =[]
            to_emails.append(receipent)
            text                        =str(request.POST.get('name'))+" from "+str(request.POST.get('industry_name'))+" has shown an interest. For details visit https://bimsnepal.com/list "
            send_mail(to_emails,text)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    
def sms_otp(request):
    var_otp                             =generate_code()
    contact_num                         =request.GET.get('contact_no')
    print(var_otp)
    contact_and_otp                     =ContactAndOTP(contact_no=contact_num,otp=var_otp)
    contact_and_otp.save()

    r                                 = requests.post(
            "http://api.sparrowsms.com/v2/sms/",
            data                      ={'token' : 'xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                                      'from'  : 'InfoSMS',
                                      'to'    : contact_num,
                                      'text'  : var_otp})
                  
    status_code                       = r.status_code
    response                          = r.text
    response_json                     = r.json()
    print(response)
    print(status_code)
    print(response_json)
    
    return render(request,'index.html')

def generate_code():
     return ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
 
class LandingPageListView(ListView):
    model                   =Contact
    template_name           ='table.html'
    #object_list will get all the objects as you can see in table.html

    
