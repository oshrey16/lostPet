from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from post.models import LostPet
from django.urls import reverse
from post.forms import comForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from twilio.rest import Client
from django.conf import settings
from lostPet.settings import EMAIL_HOST_USER


def allp(request):
    pets_list = LostPet.objects.order_by('-id')[:20]
    context = {'pets_list': pets_list}
    return render(request, "all.html", context)


def delete(request, id):
    pet = LostPet.objects.get(id=id)
    if request.method == "POST":
        pet.delete()
        return HttpResponseRedirect("/home")
    return render(request, "delete.html")


SUBJECT_STR = u"למישהו יש חדש בנושא הדיווח!!"


def bodyCreate(freetext, firstName, lastName, phone, email, hosturl, id):
    text = ""
    text += freetext
    text += "\n\n==================================\n"
    text += u"   פרטים ליצירת קשר: {} {} {} {}".format(
        firstName, lastName, phone, email)
    text += "\n\n====================\n" + \
        u"למחיקת הפרסום במידה והדיווח טופל:          "
    text += (hosturl+"delete/"+str(id))
    print(text)
    return text


def bodyCreateSMS(freetext, firstName, lastName, phone, email):
    text = ""
    text += u"למישהו יש חדש בנושא הדיווח!!\n"
    text += freetext
    text += "\n\n==================================\n"
    text += u"פרטים ליצירת קשר: {} {} {} {} ".format(
        firstName, lastName, phone, email)


def com(request, id):
    if request.method == 'GET':
        form = comForm()
    else:
        form = comForm(request.POST, request.FILES)
        # print(form.errors)
        if form.is_valid():
            pet = form.cleaned_data['pet']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            freetext = form.cleaned_data['freetext']
            try:
                new_mail = form.save()
                msgToHost = EmailMessage(
                    SUBJECT_STR,
                    bodyCreate(freetext, firstName, lastName, phone,
                               email, request.build_absolute_uri("/home/"), id),
                    EMAIL_HOST_USER,
                    [pet.pub_email],
                )
                # TODO-  UPDATE EMAIL
                # msgToHost.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            to = "+972"+pet.pub_phone
            client = Client(settings.TWILIO_ACCOUNT_SID,
                            settings.TWILIO_AUTH_TOKEN)
            try:
                response = client.messages.create(
                    body=bodyCreateSMS(freetext, firstName, lastName, phone, email), to=to, from_=settings.TWILIO_PHONE_NUMBER)
                return redirect('/home')
            except:
                return redirect('/home/errorsms')
        else:
            print("ERROR- form not ok")
    return render(request, "com.html", {'form': form, 'pet_id': id})


def aboutUs(request):
    return render(request, "aboutus.html")


def errorsms(request):
    return render(request, "errorsms.html")


def my404(request, exception):
    return render(request, "404.html")
