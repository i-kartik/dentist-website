from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'home.html', {})

def contact(request):
    if request.method=='POST':
        message_name=request.POST['message-name'] #message-email is name of the box while message_name is the vairbale name
        message_email=request.POST['message-email']
        message=request.POST['message']

        # send an Email
        send_mail(
        message_name, # subject
        message, # message
        message_email, # from email
        ['kartikkhandelwal63@gmail.com'], # to email

        )

        return render(request,'contact.html',{'message_name':message_name})
    else:
        return render(request,'contact.html', {})

def about(request):
    return render(request,'about.html',{})

def blog_details(request):
    return render(request,'blog-details.html', {})

def blog(request):
    return render(request,'blog.html', {})

def pricing(request):
    return render(request,'pricing.html', {})

def service(request):
    return render(request,'service.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def appointment(request):




            if request.method=='POST':

                your_name=request.POST['your-name'] #message-email is name of the box while message_name is the vairbale name
                your_phone=request.POST['your-phone']
                your_email=request.POST['your-email']
                your_address=request.POST['your-address']
                your_scheldule=request.POST['your-scheldule']
                your_time=request.POST['your-time']
                your_message=request.POST['your-message']
                # send an Email

                send_mail(
                'Appointment has been booked for ' +your_name, # subject
                your_message, # message
                your_email, # from email
                ['kartikkhandelwal63@gmail.com'], # to email

                )

                return render(request,'appointment.html', {'your_scheldule':your_scheldule, 'your_name': your_name})
            else:
                return render(request,'home.html', {})
