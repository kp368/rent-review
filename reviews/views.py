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
    property.price = u'£700 pcm'
    comments = property.review_set.all()
    return render(request, "leader.html", {'title':addr, 'comments':comments, 'property':property})

def comment(request, property_id):
    property = Property.objects.get(id=property_id)
    text = request.POST['comment_body']
    title = request.POST['comment_title']
    if not title:
        title = text[:95] + '...'
    r = Review(body=text, title=title, author=request.user, subject=property)
    r.save()
    return HttpResponseRedirect(reverse('reviews:property', args=(property_id,)))
    
def new(request):
    if request.method == 'GET':
        query = request.GET['q']
        property = Property()
        property.postcode = query
        return render(request, "leader.html", {'property':property, 'comments':[], 'title':'A property at ' + query})

    elif request.method == 'POST':
        property = Property()
        property.address = request.POST['new_address']
        property.postcode = request.POST['postcode']
        property.description = request.POST['description']
        property.save()
        return HttpResponseRedirect(reverse('reviews:property', args=(property.id,)))

def search(request):
    query = request.GET['q']
    property_list = Property.objects.filter(postcode=query.replace(" ", ""))
    if len(property_list) == 1:
        return HttpResponseRedirect(reverse('reviews:property', args=(property_list[0].id,)))
    elif len(property_list)==0:
        return HttpResponseRedirect(reverse('reviews:new') + '?q=' + query)
    return render(request, "list.html", {'title':"Search results for " + query, 'properties':property_list})