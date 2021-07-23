from django.views.generic import View
from django.shortcuts import render
# Create your views here.

class MainView(View):
    def get(self,request):
        return render(request,'home.html')