from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from post.models import LostPet
from django.urls import reverse
from post.forms import comForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from twilio.rest import Client
from django.conf import settings
from lostPet.settings import EMAIL_HOST_USER
import json

heb_dict = ""
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


def bodyCreate(freetext, firstName, lastName, phone, email, hosturl, id):
    text = ""
    text += freetext
    text += "\n\n====================\n"
    text += heb_dict["Words"][0]["Email"]["body"]["1"]
    text += " {} {} {} {}".format(firstName, lastName, phone, email)
    text += "\n\n====================\n"
    text += heb_dict["Words"][0]["Email"]["body"]["2"]
    # text += " {}delete/{}".format(hosturl,str(id))
    text += (" " + hosturl+"delete/"+str(id))
    return text


def bodyCreateSMS(freetext, firstName, lastName, phone, email):
    text = ""
    text += heb_dict["Words"][1]["SMS"]["Subject"]
    text += "\n"
    text += freetext
    text += "\n\n====================\n"
    text += heb_dict["Words"][1]["SMS"]["Con"]
    text += u" {} {} {} {} ".format(
        firstName, lastName, phone, email)


def com(request, id):
    if request.method == 'GET':
        form = comForm()
    else:
        with open('website/text_heb.json','rb') as json_file:
            global heb_dict
            heb_dict = json.load(json_file)
            print(heb_dict)
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
                        heb_dict["Words"][0]["Email"]["Subject"],
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

def my500(request):
    return render(request, "500.html")
