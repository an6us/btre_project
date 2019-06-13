from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check if user has made inquir already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquire for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contact.save()

        #send email 
        # send_mail(
        #     'Propertry Listing Inquiry',
        #     'There has been an inquiry for' + listing + '. Sign into the admin panel for more info ',
        #     'shoecanada@gmail.com',
        #     [realtor_email, 'adelyn101@icloud.com', 'aafriends1@gmail.com'],
        #     fail_silently=False
        # )
        subject, from_email, to = 'hello', 'shoecanada@gmail.com', 'aafriends1@gmail.com'
        text_content = 'This is an important message.'
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, 'Your requset has been submitted, a realtor will get back to you soon')

    return  redirect('/listings/'+listing_id)