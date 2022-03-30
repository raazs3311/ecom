
from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import ContactForm
from .models import  Category,Product, logo, order
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib import messages


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


def Sign(request):
    if request.method == 'POST':

       username = request.POST['username']
       Full_Name = request.POST['Full_Name']
       Email = request.POST['Email']
       Password = request.POST['Password']       
       myuser = User.objects.create_user(username, Email, Password)
       myuser.Full_Name = Full_Name
       myuser.save()
      
    
    return render(request, 'base.html')

def login(request):
    if request.method == 'POST':
        
        loginusername = request.POST.get('uname')   
        loginPassword = request.POST.get('password') 

        user = auth.authenticate(username=loginusername, password=loginPassword)  
        messages.success(request, messages.INFO, 'Loged in Successfully')
    

        if user is not None:
            auth.login(request , user)
            return redirect('acces:base')
        else:       
            return redirect('acces:base')
    return render(request , 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('acces:base') 
    
    return render(request, 'logout.html')


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

    return render(request,'details.html',{'memory':memory , 'memoryid':memoryid})

def Buy(request , id):
    buy = Product.objects.get( id = id)
    if request.method == 'POST':
    #     buy.save()
        email = request.POST.get('email')
        pro_id = request.POST.get('pro_id')
        product_1 = Product.objects.get(id = pro_id)
        # test =  order.objects.filter(email = email).id
        if order.objects.filter(email = email ,product_1 = product_1).exists():
            # test = order.objects.get(email = email )
            # test = test.id
            # test = order.objects.get(id = test)
            # count = test.count 
            # test.count = count + 1
            # test.save()            
            return HttpResponse('order already exists')

        else:
            vlu = 1
            test2 = order.objects.create(email = email , count = int(vlu) , product_1 = product_1 )            
            test2.save()
            
    return render(request,'checkout.html',{'buy':buy})

def search(request):
    query = request.GET['query']
    allproduct = Product.objects.filter(name = query)
    
    return render(request, 'search.html', {'allproduct':allproduct})





    

