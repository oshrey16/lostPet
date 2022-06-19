from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from post.models import LostPet
from django.urls import reverse
from post.forms import comForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage

def allp(request):
	pets_list = LostPet.objects.order_by('-id')[:20]
	context = {'pets_list': pets_list}
	return render(request, "all.html", context)
    
def delete(request, id):
    pet = LostPet.objects.get(id=id) 
    if request.method =="POST":
        pet.delete()
        return HttpResponseRedirect("/home")
    return render(request, "delete.html")
    
  
def com(request, id):
    if request.method == 'GET':
        form = comForm()
    else:  
        form = comForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            pet = form.cleaned_data['pet']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            freetext = form.cleaned_data['freetext']
            try:
                new_mail=form.save()
                msgToHost = EmailMessage(
                    u"פנייה חדשה : "+firstName+" "+lastName,
                    freetext+"\n\n==================================\n"+u"   פרטים ליצירת קשר: "+phone+" "+email
                    +"\n\n====================\n"+u"למחיקת הפרסום במידה והדיווח טופל:          "+"http://127.0.0.1:8000/home/delete/"+str(id), 
                    'lostpet.team@yahoo.com',
                    ['michalabr5@gmail.com'],
                )
                msgToHost.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/home')
    return render(request, "com.html", {'form': form, 'pet_id': id})

def aboutUs(request):
       return render(request, "aboutus.html")