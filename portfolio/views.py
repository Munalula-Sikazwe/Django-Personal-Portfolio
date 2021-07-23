from django.views.generic import View
from django.shortcuts import render
from .models import Contact
# Create your views here.

class MainView(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        name = request.POST.get('name','Anonymous')
        email = request.POST.get('email','Anonymous')
        subject = request.POST.get('subject','Anonymous')
        message = request.POST.get('message','Anonymous')
        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        contact.save()
        