from django.shortcuts import render,HttpResponseRedirect
from main.forms import StudentForm
from django.views.generic.base import TemplateView,RedirectView
from main.models import Student

# Create your views here.
def index(request):
    return render(request,'main/index.html')

class StudentCreate(TemplateView):
    template_name='main/addshow.html'
    def post(self,request):
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    def get(self,request):
        fm=StudentForm()
        students=Student.objects.all()
        context={'form':fm,'students':students}
        return render(request,'main/addshow.html',context)

class StudentDelete(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        stuid=kwargs['id']
        Student.objects.get(pk=stuid).delete()
        return super().get_redirect_url()
class StudentUpdate(TemplateView): 
    template_name='main/update.html'
    def get(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi) 
        context={"form":fm}
        return render(request,'main/update.html',context) 
    def post(self,request,id): 
        pi=Student.objects.get(pk=id) 
        fm=StudentForm(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
        context={"form":fm}
        return render(request,'main/update.html',context) 
        







