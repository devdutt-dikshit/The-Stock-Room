from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .forms import ProductForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


def about(request):
    return render(request,'shop/about.html')
def add_to_cart(request,uid,pid):
    try:
        prod_data=Productsitems.objects.get(pk=pid)
        cart_data=Cart.objects.filter(current_user=uid,prod_details=prod_data)
        data=str(cart_data[0].id)
        url='/updatecart/'+data+'/1'
        return redirect(url)
    except:
        prod_data=Productsitems.objects.get(pk=pid)
        cart_data=Cart(current_user=uid,prod_details=prod_data,quantity=1)
        cart_data.save()
        return redirect('/cart/'+ str(uid))


        # print(prod_data.desc)
def show_cart(request,id):
    total=0
    cart_data=Cart.objects.filter(current_user=id)
    for i in cart_data:
        if(not i.quantity):
            data=Cart.objects.get(pk=i.id)
            data.delete()
            print("deleted: ", i.prod_details.product_name)
        total=float(total+int(i.quantity)*int(i.prod_details.prize))
    params={'cartdata':cart_data,'total':total}
    return render(request,'shop/cart.html', params)

def update_cart(request,id,q):
    try:
        cart_data=Cart.objects.get(pk=id)
        uid=str(cart_data.current_user)
        cart_data.quantity=cart_data.quantity+int(q)
        cart_data.save()
        return redirect('/cart/'+ str(uid))
    except:
        print("Invalid Request")

def delete_cart_item(request,id):
    data=Cart.objects.get(pk=id)
    uid=data.current_user
    data.delete()
    return redirect('/cart/'+str(uid))

# Create your views here.
# class PersonCreateView(CreateView):
#     model = Products
#     fields = '__all__'
class Prod_view(ListView):
    model=Productsitems

def category(request):
    products=Productsitems.objects.all()
    params={'products':products}
    return render(request,'shop/category.html', params)

def index(request):
    products=Productsitems.objects.all()
    params={'products':products}
    return render(request,'shop/index.html', params)

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password1']
        if(password1==password2):
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            print("Success")   
            messages.info(request,"Registration")
            return redirect('/login')
        else:
            messages.info(request,"Password not match")
            return redirect('/register')
    else:
        return render(request,'shop/register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pw']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login")
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/login')
    else:
        return render(request,'shop/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request,"logout")
    return redirect('/')


def thnku(request):
    return render(request,'shop/thnku.html')


def search(request):
    return render(request,'shop/from.html')

@login_required(login_url='/login/')
def additem(request,id=0):
    if request.method=='POST':
        if id==0:
            form=ProductForm(request.POST, request.FILES)
            print("update54153")

        else:
            product=Products.objects.get(id=id)
            form=ProductForm(request.POST, request.FILES, instance=product)
            print("updated")
        if form.is_valid():
            form.save()
            return redirect('/shop')
        else:
            return redirect('/shop/additem')

    else:
        if id==0:
            form=ProductForm()
        else:
            product=Products.objects.get(id=id)
            form=ProductForm(instance=product)
    return render(request,'shop/contact.html',{'form':form})

def delete_view(request, id):
    product=Products.objects.get(id=id)
    # form=ProductForm(instance=product)
    product.delete()
    return redirect('/shop')
    # return render(request,'shop/contact.html',)

def productview(request, pk):
    product=Productsitems.objects.filter(pk=pk)
    productall=Productsitems.objects.all()
    data={'product':product, 'allproducts': productall}
    return render(request,'shop/pdp.html',data)


def checkout(request):
    return render(request,'shop/checkout.html')


def filterprods(request, cat):
    cat1=Productcat.objects.get(prodcat=cat)
    cat=cat1.id
    data=Productsitems.objects.filter(prodcat=cat)
    return render(request,'shop/category.html', {'products':data})

def a(request):
    if request.method=='POST':
        print("in POST")
        return HttpResponse("<h1>POST</h1>")
    
    return render(request,'shop/test.html')