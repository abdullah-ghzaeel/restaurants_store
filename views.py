from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from .models import Resturant
import random
# Create your views here.
#def home(request):
 #   html_var='f strings'
   # html_ =f"""<!doctype html>
    #<html lang="en">
    #<head>my first app
    #</head>
    #<body>
    #<h1>hello world!</h1>
    #<p>this is {html_var} coming through</p>
    #</body>
    #</html>"""
    #return HttpResponse(html_)
def home(request):
    num=random.randint(0,10000)
    return render(request,"home.html",{"html_var": True, "num": num})
def home1(request):
    num1=random.randint(0,100000)
    return render(request,"about.html",{"html_var": True, "num": num1})
def home2(request):
    num2=random.randint(0,100000)
    return render(request,"contact.html",{"html_var": True, "num": num2})
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"contact.html",{})
class ContactTemplateView(TemplateView):
    template_name="contact.html"
    #def get(self, request,*args, **kwargs):
class AboutTemplateView(TemplateView):
    template_name="about.html"
# class HomeTemplateView(TemplateView):
#     template_name="home.html"
#     def get_context_data(self,*args,**kwargs):
#         context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
#         print(context)
#         num=random.randint(0,10000) 
#         context={ "num":num }
#         return context 
def resturants_listview(request):
    template_name='resturants/resturants_list.html'
    queryset = Resturant.objects.all()
    context={
        "object_list" : queryset
    }
    return render(request, template_name, context)
class ResturantListView(ListView):
    queryset = Resturant.objects.all()
class MexicanResturantListView(ListView):
    queryset = Resturant.objects.filter(category__iexact='mexican')
    template_name='resturants/resturants_list.html'
class AsianturantListView(ListView):
    queryset = Resturant.objects.filter(category__iexact='asian')
    template_name='resturants/resturants_list.html'
class ResturantDetaiView(DetailView):
    queryset = Resturant.objects.all()
    def get_context_data(self,*args, **kwargs):
        print(self.kwargs)
        context = super(ResturantDetaiView,self).get_context_data(*args,**kwargs)
        print(context)
        return context
