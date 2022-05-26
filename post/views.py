from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import postForm
from django.urls import reverse
from post.models import LostPet
from django.core.mail import send_mail, BadHeaderError, EmailMessage

def index(request):
    if request.method == 'GET':
        form = postForm()
    else: 
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            pub_date = form.cleaned_data['pub_date']
            pub_name = form.cleaned_data['pub_name']
            pub_phone = form.cleaned_data['pub_phone']
            pub_email = form.cleaned_data['pub_email']
            animal_type = form.cleaned_data['animal_type']
            animal_status = form.cleaned_data['animal_status']
            animal_location = form.cleaned_data['animal_location']
            animal_freetext = form.cleaned_data['animal_freetext']
            animal_image = form.cleaned_data['animal_image']
            new_post=form.save()
            return redirect('/home')
    return render(request, "post.html", {'form': form})
       
       
