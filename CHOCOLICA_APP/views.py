from django.shortcuts import render,redirect
from CHOCOLICA_APP.models import admindb,categorydb,productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def addadminpage(request):
    return render(request,"AddAdmin.html")
def saveadmindata(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        mb=request.POST.get('mobile')
        em=request.POST.get('email')
        im=request.FILES['image']
        un=request.POST.get('username')
        pw=request.POST.get('password')
        cp=request.POST.get('confirm')
        obj=admindb(Name=nm,Mobile=mb,Email=em,Image=im,Username=un,Password=pw,Confirm=cp)
        obj.save()
        return redirect(displayadminpage)
def displayadminpage(request):
    data=admindb.objects.all()
    return render(request,"DisplayAdmin.html",{'data':data})
def editadmindata(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,"EditAdmin.html",{'data':data})
def updateadmindata(request,dataid):
    if request.method=="POST":
        nm=request.POST.get('name')
        mb=request.POST.get('mobile')
        em=request.POST.get('email')
        un=request.POST.get('username')
        pw=request.POST.get('password')
        cp=request.POST.get('confirm')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=nm,Mobile=mb,Email=em,Image=file,Username=un,Password=pw,Confirm=cp)
        return redirect(displayadminpage)
def deleteadmindata(request,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadminpage)
def addcategorypage(request):
    return render(request,"AddCategory.html")
def savecategorydata(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        ds=request.POST.get('description')
        ci=request.FILES['cimage']
        obj=categorydb(Category_Name=cn,Description=ds,Category_Image=ci)
        obj.save()
        return redirect(displaycategorypage)
def displaycategorypage(request):
    data=categorydb.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def editcategorydata(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,"EditCategory.html",{'data':data})
def updatecategorydata(request,dataid):
    if request.method=="POST":
        cn=request.POST.get('cname')
        ds=request.POST.get('description')
        try:
            ci=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(ci.name,ci)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Category_Image
        categorydb.objects.filter(id=dataid).update(Category_Name=cn,Description=ds,Category_Image=file)
        return redirect(displaycategorypage)
def deletecategorydata(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategorypage)
def addproductpage(request):
    data=categorydb.objects.all()
    return render(request,"AddProducts.html",{'data':data})
def saveproductdata(request):
    if request.method=="POST":
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        pd=request.POST.get('pdescription')
        pi=request.FILES['pimage']
        ca = request.POST.get('pcategory')
        obj=productdb(Product_Name=pn,Price=pr,Quantity=qt,Product_Description=pd,Product_Image=pi,Category=ca)
        obj.save()
        return redirect(displayproductpage)
def displayproductpage(request):
    data=productdb.objects.all()
    return render(request,"DisplayProducts.html",{'data':data})
def editproductdata(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    print(data)
    return render(request,"EditProducts.html",{'data':data,'da':da})
def updateproductdata(request,dataid):
    if request.method=="POST":
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        pd=request.POST.get('pdescription')
        ca = request.POST.get('pcategory')

        try:
            pi=request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(pi.name,pi)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Product_Image
        productdb.objects.filter(id=dataid).update(Product_Name=pn,Price=pr,Quantity=qt,Product_Description=pd,Product_Image=file,Category=ca)
        return redirect(displayproductpage)
def deleteproductdata(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproductpage)
def loginpage(request):
    messages.success(request, "Login Successfull!!")
    return render(request,"Login.html")
def savelogindata(request):
    if request.method=="POST":
        Username_c=request.POST.get('username')
        Password_c=request.POST.get('password')
        if User.objects.filter(username__contains=Username_c).exists():
            user=authenticate(username=Username_c,password=Password_c)
            if user is not None:
                login(request,user)
                request.session['username']=Username_c
                request.session['password']=Password_c
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def logoutpage(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def displaymessage(request):
    data=contactdb.objects.all()
    return render(request,"Messages.html",{'data':data})


