from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
     return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name =  request.POST['message-name']
        message_email =  request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            message_name,
            message,
            message_email,
            ['bedisarabpreet@gmail.com'],
            
            )
        
        return render(request, 'contact.html', {'message_name':message_name})
        
    else:
        return render(request, 'contact.html', {})
    
    
def about(request):
     return render(request, 'about.html', {})  

def pricing(request):
     return render(request, 'pricing.html', {})   

def service(request):
     return render(request, 'service.html', {}) 

    
def appointment(request):
    if request.method == "POST":
        
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address =request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date  = request.POST['your-date']
        your_message = request.POST['your-message']
        
        appointment = "Name:" +  your_name + "\nPhone:"  + your_phone + "\nEmail:" + your_email + "\nAddress:" + your_address + "\nSchedule:" + your_schedule  + "\nDay:" + your_date  + "\nMessage:"  + your_message  
        send_mail(
           'Appointment Reqquest',
            appointment,
            your_email,
            ['bedisarabpreet@gmail.com'],
            
            )
        
        return render(request, 'appointment.html', {'your_name':  your_name,
                                                   'your_phone': your_phone ,
                                                   'your_email': your_email,
                                                   'your_address': your_address,
                                                   'your_schedule': your_schedule,
                                                   'your_date': your_date,
                                                   'your_message': your_message
                                                   })
        
    else:
        return render(request, 'home.html', {})
    
    
def newsletter(request):
    if request.method == "POST":
        
        nl_email = request.POST['nl-email']
        newsletter = "Weekly Newsletter sent to your email address."
        
        newsletter = "Weekly Newsletter Sent Demo"
        send_mail(
           'Weekly Newsletter Request',
            newsletter,
            nl_email,
            ['bedisarabpreet@gmail.com'],
            
            )
        
        return render(request, 'newsletter.html', {'nl_email': nl_email
                                                   })
        
    else:
        return render(request, 'home.html', {})    