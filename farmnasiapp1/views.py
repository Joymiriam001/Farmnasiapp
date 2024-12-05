import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Agriculturalwebsite2.settings")
django.setup()

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def seasons(request):
    return render(request, 'seasons.html')
def product(request):
    return render(request, 'product.html')
def cereals(request):
    return render(request, 'cereals.html')
def beverage(request):
    return render(request, 'beverage.html')
def fruits(request):
    return render(request, 'fruits.html')
def vegetables(request):
    return render(request, 'vegetables.html')
def legumes(request):
    return render(request, 'legumes.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from farmnasiapp1.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Option 1: Send email
            send_mail(
                subject,
                message,
                email,
                [settings.EMAIL_RECIPIENT],
                fail_silently=False,
            )

            # Option 2: Store in database (optional)
            # Contact.objects.create(name=name, email=email, subject=subject, message=message)

            return redirect('contact')  # Redirect to the contact page after success

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


from django.core.mail import send_mail

try:
    send_mail(
        'Subject here',
        'Here is the message.',
        os.getenv('EMAIL_HOST_USER'),
        [os.getenv('EMAIL_RECIPIENT')],
        fail_silently=False,
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
