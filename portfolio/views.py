from django.shortcuts import render,redirect,reverse
from django.views.generic import View

from .models import Contact,AboutMe


# Create your views here.

class MainView(View):
    def get(self, request):
        aboutme = AboutMe.objects.first()
        context = { 'aboutme':aboutme}
        return render(request, 'home.html',context)

    def post(self, request):
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', 'Anonymous')
        subject = request.POST.get('subject', 'Anonymous')
        message = request.POST.get('message', 'Anonymous')
        contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        contact.save()
        return  redirect(reverse('portfolio:home'))