from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    data='cRicKet is My FavoRite GaME'
    d={'data':data}
    return render(request,'built_in_filters.html',d)