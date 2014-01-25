# -*- coding: utf-8 -*- 
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Property, Review

def index(request):
	return HttpResponse("Hello")

def property(request, property_id):
	property = Property.objects.get(id=property_id)
	addr = property.address
	price = u'£700 pcm'
	comments = property.review_set.all()
	return render(request, "index2.html", {'address':addr, 'price':price, 'title':addr, 'comments':comments, 'property':property, 'current_user':request.user})

def comment(request, property_id):
	property = Property.objects.get(id=property_id)
	text = request.POST['comment_body']
	r = Review(body=text, author=request.user, subject=property, rating=4)
	r.save()
	return HttpResponseRedirect(reverse('reviews:property', args=(property_id,)))
	
def search(request):
	query = request.GET['q']
	property_list = Property.objects.filter(postcode=query.replace(" ", ""))
	if len(property_list) == 1:
		return HttpResponseRedirect(reverse('reviews:property', args=(property_list[0].id,)))
	return HttpResponse(query)