from django.shortcuts import render, redirect
from django.contrib import messages
from .form import InquiryForm
from .models import Course, Testimonial
from django.core.mail import send_mail
from django.conf import settings

# Inquiry View
def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Extract user input from form
            first_name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            state = form.cleaned_data['state']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            # Create email content
            email_subject = "New Inquiry from Website"
            email_body = (
                f"First Name: {first_name}\n"
                f"Phone: {phone}\n"
                f"Age: {age}\n"
                f"State: {state}\n"
                f"Address: {address}\n"
                f"Email: {email}\n\n"
                f"subject:{subject}\n\n"
                f"Inquiry Message:\n{message}"
            )

            # Send email to admin
            try:
                # Send email to admin
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.EMAIL_HOST_USER, 
                    recipient_list=[settings.ADMIN_EMAIL], 
                    fail_silently=False,
                )
                # Provide feedback to the user
                messages.success(request, "Your inquiry has been sent successfully!")
                return redirect("success")  
            
            except Exception as e:
                # Handle email errors
                messages.error(request, f"Failed to send inquiry: {str(e)}")
                return render(request, 'main/inquiry.html', {'form': form})

    else:
        form = InquiryForm()

    return render(request, 'main/inquiry.html', {'form': form})

# Home View
def home(request):
    return render(request, 'main/home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Courses View
def courses(request):
    courses = Course.objects.all()
    return render(request, 'main/about_courses.html', {'courses': courses})

# About Founder View
def about_founder(request):
    return render(request, 'main/about_founder.html')

# Testimonials View
def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def success(request):
    return render(request, 'main/sucess.html')
