from django.views.generic import View
from django.shortcuts import render
# Create your views here.

class MainView(View):
    def get(self):
        return render(self.request,'home.html')