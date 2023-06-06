from django.shortcuts import render,redirect
from .models import Product
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request, 'productinput.html')
class Insert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p=Product(pid=p_id, pname=p_name, pcost=p_cost, pmfdt=p_mfdt, pexpdt=p_expdt)
        p.save()
        return HttpResponse("product inserted successfully")
class Display(View):
    def get(self, request):
        qs=Product.objects.all()
        condic={"records":qs}
        return render(request,'display.html', context=condic)
class DeleteInput(View):
    def get(self, request):
        qs=Product.objects.all()
        condic={"records":qs}
        return render(request, 'deleteinput.html', context=condic)
class Delete(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p=Product.objects.get(pid=p_id)
        p.delete()
        return redirect('/productapp/display')