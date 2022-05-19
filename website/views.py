from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from post.models import LostPet

def allp(request):
	pets_list = LostPet.objects.order_by('-id')[:20]
	context = {'pets_list': pets_list}
	return render(request, "all.html", context)