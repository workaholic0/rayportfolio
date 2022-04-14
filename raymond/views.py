
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    '''displays the home'''
    if request.method=='POST':
        name= request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,email,message)
    send_mail(
    'Hello',
    f'Name: {name}\n\nEmail:{email}\n\nMessage:{message} this is the message.',
    'techgeek337@gmail.com',
    ['raymondagholor0@gmail.com'],
    fail_silently=False,
    )
    return render(request, 'index.html')
