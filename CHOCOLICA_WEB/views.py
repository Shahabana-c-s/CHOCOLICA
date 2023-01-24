from django.shortcuts import render,redirect
from CHOCOLICA_APP.models import categorydb,productdb,contactdb
from CHOCOLICA_WEB.models import customerdetailsdb



# Create your views here.
def home(request):
    data=categorydb.objects.all()
    return render(request,"home.html",{'data':data})
def about(request):
    data=categorydb.objects.all()
    return render(request,"about.html",{'data':data})
def contact(request):
    data=categorydb.objects.all()
    return render(request,"contact.html",{'data':data})
def chocolate(request):
    data = categorydb.objects.all()
    dat=productdb.objects.all()
    return render(request,"chocolates.html",{'dat':dat,'data':data})
def discategorypage(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    data=categorydb.objects.all()
    products=productdb.objects.filter(Category=itemCatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"DisCategory.html",context)
def singleproductpage(request,dataid):
    da=categorydb.objects.all()
    data=productdb.objects.get(id=dataid)
    return render(request,"SingleProduct.html",{'dat':data,'da':da})
def customerdetailspage(request):
    return render(request,"CustomerDetails.html")
def savecustomerdetails(request):
    if request.method == "POST":
        cn = request.POST.get('username')
        ce = request.POST.get('cemail')
        cp = request.POST.get('password')
        cc = request.POST.get('cconfirm')
        if cp == cc:
            obj = customerdetailsdb(username=cn, CEmail=ce, password=cp, CConfirm=cc)
            obj.save()
            return redirect(customerloginpage)
        else:
            return render(request, "CustomerDetails.html", {'msg': "sorry..password not matched"})
def customerloginpage(request):
    return render(request,"CustomerLogin.html")
def savecustomerlogin(request):
    if request.method == "POST":
        username_c = request.POST.get('username')
        password_c = request.POST.get('password')
        if customerdetailsdb.objects.filter(username=username_c,password=password_c).exists():
            # data=customerdetailsdb.objects.filter(username=username_c,password=password_c).values('email','id').first()
            request.session['username']=username_c
            request.session['password']=password_c
            # request.session['email'] =data['email']
            # request.session['userid'] =data['id']
            return redirect(home)
        else:
            return render(request,"CustomerLogin.html",{'msg':"Sorry..Invalid Username or Password"})
def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect (home)
def savecontact(request):
    if request.method == "POST":
        yn = request.POST.get('contactname')
        ye = request.POST.get('contactemail')
        ys = request.POST.get('subject')
        ym = request.POST.get('message')
        obj = contactdb(Cname=yn,Cemail=ye,Subject=ys,Message=ym)
        obj.save()
        return redirect(contact)
# def Addtocart(request):