from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from post.models import LostPet
from django.urls import reverse
from post.forms import comForm

def allp(request):
	pets_list = LostPet.objects.order_by('-id')[:20]
	context = {'pets_list': pets_list}
	return render(request, "all.html", context)
    
def delete(request, id):
  pet = LostPet.objects.get(id=id)
  pet.delete()
  return HttpResponseRedirect(reverse(allp))    
  
def com(request, id):
    if request.method == 'GET':
        form = comForm()
    else:  
        form = comForm(request.POST, request.FILES)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            freetext = form.cleaned_data['freetext']
            new_post=form.save()
            return redirect('/home')
    return render(request, "com.html", {'form': form})     