from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.contrib.messages import success
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
        success(request,"Thank you for reaching out I will respond as soon as I can")
        return  redirect(reverse('portfolio:home'))