from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'bsicapp/index.html')
def form_name_view(request):
    form=forms.FormName()
    if request.method =='POST':
        form=forms.FormName(request.POST)
        if foorm.is_valid():
            print("validation is succesful")
            print(form.cleaned_data['name'])

    return render(request,'bsicapp/forms.html',{'form':form})
