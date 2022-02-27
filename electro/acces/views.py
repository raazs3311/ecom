import email
from itertools import count

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import ContactForm
from .models import  Category,Product, logo, order

# Create your views here.

def base(request):
    
    
    cat = Category.objects.all()
    
    pro = Product.objects.all()
    form = ContactForm(request.POST)
    Logo = logo.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    
    return render(request, 'index.html',{'cat':cat,'pro':pro, 'form':form, 'Logo':Logo})


def category(request):
    var = Category.objects.all()
    
    return render(request, 'category.html',{'var':var})
def product(request):
    pro = Product.objects.all()
    return render(request, 'product.html',{'pro':pro})
def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    
    return render(request, 'contact.html',{'form':form})

def detail(request,id):
    memory = Product.objects.get(id = id)
    memoryid = id

    # if request.method == 'POST':
    # #    memory.delete()
    # #    return redirect('/product')
    # # pass

    return render(request,'details.html',{'memory':memory , 'memoryid':memoryid})

def Buy(request , id):
    buy = Product.objects.get( id = id)
    if request.method == 'POST':
    #     buy.save()
        email = request.POST.get('email')
        pro_id = request.POST.get('pro_id')
        product_1 = Product.objects.get(id = pro_id)
        # test =  order.objects.filter(email = email).id
        if order.objects.filter(email = email ,product_1 = product_1).exists() :
            # test = order.objects.get(email = email )
            # test = test.id
            # test = order.objects.get(id = test)
            # count = test.count 
            # test.count = count + 1
            # test.save()
            print('sonam gussa nhi hai')
            return HttpResponse('order already exists')

        else:
            vlu = 1
            test2 = order.objects.create(email = email , count = int(vlu) , product_1 = product_1 )
            print('sonam gussa hai')
            test2.save()


            
    return render(request,'checkout.html',{'buy':buy})

def search(request):
    query = request.GET['query']
    allproduct = Product.objects.filter(name = query)
    
    return render(request, 'search.html', {'allproduct':allproduct})
    

