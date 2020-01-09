from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from webapp import forms

# Create your views here.
def Empview(request):
    form=forms.EmpForm()
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print('Form Data inserted successfully')
            form.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    return render(request,'welcome.html',{'form':form})
def thanksview(request):
    return render(request,'Thanks.html')
