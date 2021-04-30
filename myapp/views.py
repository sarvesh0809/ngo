from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from myapp.models import Ngoform,Validedform,AfterPayment,Contact
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from quoters import Quote
# Create your views here.
def ngoform(request):
    
    if request.method=="POST":          
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['zip']
        details=request.POST['details'] 
        phone=request.POST['phone']
        aadhar=request.POST['aadhar']
        bank_details=request.POST['bd']
        m1file=request.FILES['file1']
        m2file=request.FILES['file2']
        m3file=request.FILES['file3']
            # print(name,email,address,city,state,zipcode,details,phone)
        if len(email)<4:
            messages.warning(request,'Please fill the form correctly!')
        else:
            ins= Ngoform(name=name,email=email,aadhar=aadhar,address=address,phone=phone,city=city,state=state,zipcode=zipcode,details=details,m1file=m1file,m2file=m2file,m3file=m3file,bank_detail=bank_details)
            ins.save()
            messages.success(request,'Successfully Submitted.!')
        
  
    return render(request,'ngoform.html')


def donate(request):
    if request.user.is_authenticated:
        form = Validedform.objects.all()
        user=request.user
        full_name=user.get_username()
        print(full_name)
        params={
            'form':form,
            'full_name':full_name
        }
        return render(request,'donate.html',params)
    else:
        return HttpResponseRedirect('/login/')



def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:

                    login(request,user)
                    messages.success(request,'Welcome  !!')
                    return HttpResponseRedirect('/donate/')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/donate/')


def user_signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def index(request):
    sr=Quote.print_anime_quote()
    context={
            "sr":sr
        }
    return render(request,'index.html',context)



def contact(request):
    
    if request.method == "POST":
        email = request.POST['email']
        details = request.POST['details']
        if len(email)<8 or len(details)<10:
            messages.warning(request,'Please fill the form correctly!')
        else:
            contact=Contact(email=email,details=details)
            contact.save()
            messages.success(request,'Successfully Submitted.!')

    return render(request,'contact.html')


def afterpay(request):
    if request.user.is_authenticated:
        if request.method=="POST" :
            uname = request.POST['uname']
            ufile = request.FILES['ufile']    
            if 'image' in request.FILES['ufile'].content_type:
                pay=AfterPayment(uname=uname,ufile=ufile)
                pay.save()
                messages.success(request,'Successfully Submitted.!')
                
                # Some code
            else:
                # the file is not image
                messages.warning(request,'Please choose a proper file format .!')
        

        return render(request,'afterpay.html')

    else:
        return HttpResponseRedirect('/login/')


def error(request): 
    sr=Quote.print_anime_quote()
    context={
            "sr":sr
        }
    return render(request,'error.html',context)