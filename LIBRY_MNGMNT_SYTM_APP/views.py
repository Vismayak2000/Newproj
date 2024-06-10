
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from . models import Category,members,Book,Issue
from django.core.paginator import  Paginator,EmptyPage,InvalidPage
from datetime import date

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    d0 = date(2008, 8, 18)
    d1 = date(2008, 9, 26)
    delta = d1 - d0
    print(delta. days)
    courses_list=Book.objects.all()
    pagintor=Paginator(courses_list,9)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1

    try:
        courses=pagintor.page(page)
    except (EmptyPage,InvalidPage):
       courses=pagintor.page(pagintor.num_pages)

    return render(request,'home.html',{'books':courses})
def admin_home(request):
    return render(request,'admin_home.html')
def user_home(request):
    
    courses_list=Book.objects.all()
    pagintor=Paginator(courses_list,9)
    try:
        page=int(request.GET.get('page',1))
        
    except:
        page=1

    try:
        courses=pagintor.page(page)
    except (EmptyPage,InvalidPage):
       courses=pagintor.page(pagintor.num_pages)
    context={'books':courses}
    return render(request,'user_home.html',context)

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                
                login(request,user)
                
                return redirect('admin_home')
            else:
                auth.login(request,user)
                
                return redirect('user_home')
                
        else:
            
            messages.error(request,'Invalid Username or Password')
            return redirect('home')
            


        



"""if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pwd']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
                    if user.is_staff:
                        login(request,user)
                        return redirect('admin_home')
                    else:
                        auth.login(request,user)
                        messages.info(request, f'Welcome {username}')
                        return redirect('user_home')
        else:
            return redirect("home")"""

       
  
    

def usercreate(request):
    if request.method=='POST':
        fname=request.POST['fname'].upper()
        lname=request.POST['lname'].upper()
       
        adr=request.POST['address']
        email=request.POST['email']
        dob=request.POST['dob']
        
        img=request.FILES.get('img')
        scontact=request.POST['phone']
        psw=request.POST['psw']
        n=fname[3:].upper()
        c=scontact[-3:]
        mid="SRS"+"101"+n+c
        usr=email
        
        

          #  password matching......
        if User.objects.filter(username=usr).exists(): #check Username Already Exists..
                
                #print("Username already Taken..")
                return render(request,'home.html',messages.error(request, 'This username already exists!!!!!!'))
        else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=usr,
                    password=psw,
                    email=email
                    )
                user.save()
                member=members(fname=fname,
                                lname=lname,
                                username=usr,
                                dob=dob,
                            
                               Address=adr,
                               
                               email=email,
                               phone=scontact,
                               Photo=img,
                               MID=mid,
                               
                               )
                member.save()
                
                
                
                print("Successed...")
                
                subject = 'welcome to SRS PUBLIC LIBRARY'
                message = f'Hi {fname}, thank you for  registering in \n. USERNAME:{usr} \n PASSWORD:{psw}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                print(email_from)
                
                return render(request,'home.html',messages.success(request, 'SuccessFully Registerd...Your username and Password send to your mail id'))
    else:
        messages.error(request, 'Invalid data')

         
   
    return render(request,'home.html')



def add_category(request):
    return render(request,'add_category.html')

def category(request):
    
    if request.method == 'POST':
        cname=request.POST['cname']
        desc=request.POST['desc']
        img=request.FILES.get('img')
        if cname=="":
             return redirect('add_category')
        else:

            data = Category(name=cname,description=desc,image=img)
            data.save()
            return redirect('add_category')

def add_books(request):
    category=Category.objects.all()
    context={'category':category}
    return render(request,'add_books.html',context)
def books(request):
    if request.method=='POST':
        name=request.POST['bname']
        price=request.POST['price']
        stock=request.POST['stock']
        author=request.POST['bauthr']
        year=request.POST['year']
        language=request.POST['language']
        img=request.FILES.get('img')
        select=request.POST['select']
        if select=='---SELECT CATEGORY---':
            return redirect('add_books')

        category=Category.objects.get(id=select)
        desc=request.POST['desc']
        if name=="":
            return redirect('add_books')
        else:

            data =Book(Name=name,price=price,category=category,Photo=img,stock=stock,Author=author,language=language,desc=desc,available=True,year=year)
            data.save()
            return redirect('admin_home')

def show_customers(request):
    member=members.objects.all()
    return render(request,'show_customer.html',{'members':member})
def show_books(request):
    book=Book.objects.all()
    return render(request,'show_books.html',{'book':book})

def delete(request,pk):
    student=members.objects.get(id=pk)
    student.delete()

def edit_books(request,pk):
    products=Book.objects.get(id=pk)
    return render(request,'edit_books.html',{'products':products})
def edit_book_details(request,pk):
    if request.method=='POST':
        
        products = Book.objects.get(id=pk)
        old=products.Photo
        new=request.FILES.get('img')
        if old !=None and new==None:
            products.Photo=old
        else:
            products.Photo=new
            

        products.Name = request.POST.get('bname')
         
        products.price=request.POST['price']
        products.stock=request.POST['stock']
        products.Author=request.POST['bauthr']
        products.year=request.POST['year']
        products.language=request.POST['language']
        products.desc=request.POST['desc']
        products.save()
        #print(old)
       # print(request.FILES.get('img'))
        return redirect('show_books')
    return render(request, 'edit_books.html')

def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        name=current_user.username
        customers=members.objects.get(username=name)
        return render(request,'profile.html',{'student':customers})

def edit_profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        name=current_user.username
        customers=members.objects.get(username=name)
    
        return render(request,'edit_profile.html',{'customer':customers})

def edit_profile_details(request,pk):
      if request.method=='POST':
        
        customers = members.objects.get(id=pk)
        old=customers.Photo
        new=request.FILES.get('img')
        if old !=None and new==None:
            customers.Photo=old
        else:
            customers.Photo=new
            

        customers.fname = request.POST.get('fname')
        customers.lname=request.POST.get('lname')
        customers.username=request.POST.get('username')
        customers.Address = request.POST.get('address')
        customers.email = request.POST.get('email')
        customers.phone = request.POST.get('phone')
        customers.dob=request.POST.get('dob')
        
        customers.save()
        #print(old)
       # print(request.FILES.get('img'))
        return redirect('profile')
      return render(request, 'edit_profile.html')
 
def search(request):
    if request.method=='POST':
        s=request.POST['search']
        print(s)
        try:
           book=Book.objects.get(Name=s)
           return render(request,'search.html',{'book':book})
           
        except:
            msg="Book not Found"
            return render(request,'not_found.html',{'message':msg})

def book_details(request,pk):
    products=Book.objects.get(id=pk)
    return render(request,'book_details.html',{'books':products})

def request_issue(request,pk):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        book=Book.objects.get(id=pk)
        member=members.objects.get(username=usr)
        data=Issue(usr=member,book=book)
        data.save()
        return redirect('user_home')


def delete(request,pk):
    member=members.objects.get(id=pk)
    usr=member.username
    mem=User.objects.get(username=usr)
    mem.delete()
    member.delete()
    return redirect('show_customers')
def delete_books(request,pk):
    book=Book.objects.get(id=pk)
    
    
    book.delete()
    return redirect('show_books')

def logout(request):
	auth.logout(request)
	return redirect('home')


def user_issue(request):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        member=members.objects.get(username=usr)
        mid=member.id
        book=Issue.objects.filter(usr_id=mid,status=1)
        print(mid)
        context={'book':book}

        return render(request,'user_issue.html',context)

def user_issued(request):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        member=members.objects.get(username=usr)
        mid=member.id
        book=Issue.objects.filter(usr_id=mid,status="ISSUED")

        print(mid)
        context={'book':book}

        return render(request,'user_issed.html',context)

def admin_issue(request):
    issue=Issue.objects.filter(status=1)
    context={'book':issue}
    return render(request,'admin_issue.html',context)

def admin_issued(request):
    issue=Issue.objects.filter(status="ISSUED")
    context={'book':issue}
    return render(request,"admin_issued.html",context)



def issue_book(request,pk):
    issue=Issue.objects.get(id=pk)
    bname=issue.book.Name
    book=Book.objects.get(Name=bname)
    book.stock-=1
    book.save()
    print(issue.book.Name)
    issue.status="ISSUED"
    issue.book.stock-=1
        
    issue.save()
    return redirect('admin_issue')

def cancel_book(request,pk):
    issue=Issue.objects.get(id=pk)
    issue.status="CANCEL"
    issue.save()
   
    return redirect('admin_issue')

def return_book(request):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        member=members.objects.get(username=usr)
        mid=member.id
        book=Issue.objects.filter(usr_id=mid,status="ISSUED")
        
        context={'book':book}

        return render(request,'user_return.html',context)

def returned_book(request,pk):
    issue=Issue.objects.get(id=pk)
   
    bname=issue.book.Name
    book=Book.objects.get(Name=bname)
    issdate=str(issue.issuedate.day)+'-'+str(issue.issuedate.month)+'-'+str(issue.issuedate.year)
    expdate=str(issue.expirydate.day)+'-'+str(issue.expirydate.month)+'-'+str(issue.expirydate.year)
    days=(date.today()-issue.issuedate)
    print(date.today())
    d=days.days
    fine=0
    if d>15:
        day=d-15
        fine=day*10
        issue.fine=fine
        issue.save()
    else:
        fine=0
        issue.fine=fine
        issue.save()
    print(issue.book.Name)
    issue.status="RETURN"
    
        
    issue.save()
    return redirect('return_book')

def return_books(request):
    issue=Issue.objects.filter(status="RETURN")
    context={'book':issue}
    return render(request,"return_book.html",context)


def return_approve(request,pk):
    issue=Issue.objects.get(id=pk)
    date=issue.expirydate
    print(date)
    bname=issue.book.Name
    book=Book.objects.get(Name=bname)
    book.stock+=1
    book.save()
    issue.status="FINE"
    
    issue.save()
    return redirect('return_books')

def penalty(request,pk):
    if request.method=='POST':
        issue=Issue.objects.get(id=pk)
        name=request.POST['username']
        reason=request.POST['select']
        if name=='':
            name=0
            reason=""
        issue.penalty=name
        issue.reason=reason
        issue.save()
		
       
    return redirect('return_books')
	    
def user_penalty(request):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        member=members.objects.get(username=usr)
        mid=member.id
        book=Issue.objects.filter(usr_id=mid,status="OK")
        
        
        print(mid)
        context={'book':book}

        return render(request,'user_penalty.html',context)
    
def payment(request,pk):
    issue=Issue.objects.get(id=pk)
    issue.status="OK"
    issue.save()
    return redirect('admin_penalty')
        
   
    return redirect('user_penalty')
def admin_penalty(request):
    issue=Issue.objects.filter(status="FINE")
    for i in issue:
            total=i.fine+i.penalty+i.book.price
            i.total=total
            print(i.total)
            i.save()
    context={'book':issue}
    return render(request,"admin_penalty.html",context)

def ok(request,pk):
    issue=Issue.objects.get(id=pk)
    issue.delete()
    return redirect('user_penalty')

def cancelled_book(request):
    if request.user.is_authenticated:
        current_user = request.user
        usr=current_user.username
        member=members.objects.get(username=usr)
        mid=member.id
        book=Issue.objects.filter(usr_id=mid,status="CANCEL")

        print(mid)
        context={'book':book}

        return render(request,'cancel_book.html',context)
    





