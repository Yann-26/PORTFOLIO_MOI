from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from portbackend.models import Subscriber
from .models import *



def testimonial_list(request):
    testimonials = Testimonial.objects.all().values()
    return JsonResponse(list(testimonials), safe=False)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        subscriber = Subscriber(email=email)
        subscriber.save()

        # Envoi d'un e-mail de confirmation
        subject = 'Confirmation de votre inscription à notre newsletter'
        message = 'Bonjour, \n\nMerci de vous être abonné à notre newsletter.'
        from_email = 'votre@email.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})