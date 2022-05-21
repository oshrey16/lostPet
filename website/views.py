from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from post.models import LostPet
from django.urls import reverse

def allp(request):
	pets_list = LostPet.objects.order_by('-id')[:20]
	context = {'pets_list': pets_list}
	return render(request, "all.html", context)
    
def delete(request, id):
  pet = LostPet.objects.get(id=id)
  pet.delete()
  return HttpResponseRedirect(reverse(allp))    
  
     