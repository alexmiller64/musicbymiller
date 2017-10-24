from django.shortcuts import render
from hello.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def get_index(request):
    return render(request, 'blogposts.html')


def get_about(request):
    return render(request, 'about.html')


def get_contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('touch contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['alexander.dean.miller@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('/sent')

    return render(request, 'contact.html', {
        'form': form_class,
})


def get_payment(request):
    return render(request, 'payment.html')


def sent(request):
    return render(request, 'sent.html')
