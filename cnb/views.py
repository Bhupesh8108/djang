from django.shortcuts import HttpResponse,render 

def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return HttpResponse('This is a product')
def order(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    number = request.POST.get('number')
    print(name, address, number)
    return render (request,'order.html')
def carrier(request):
    return HttpResponse('This is career website')