from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *


def listStaff(request):
    accountlist = Account.objects.filter(lever=1)
    context = {
        'accountlist':accountlist,
        }
    return render(request, 'staff/accountstaff/list.html',context)

def createstaff(request):
    Cstaff = CreateAccountStaffForm()
    if request.method == 'POST':
        Cstaff = CreateAccountStaffForm(request.POST)
        if Cstaff.is_valid():
            Cstaff.save()
            return redirect('list-staff')
    ctx = {'Cstaff':Cstaff}
    return render(request,'staff/accountstaff/staff_form.html', ctx)
    

def infostaff(request, pk):
    account = get_object_or_404(Account, pk=pk)
    context ={
        'account':account
        }
    return render(request, 'staff/accountstaff/infostaff.html', context)

def listUser(request):
    userlist = Account.objects.filter(lever=2)
    context = {'userlist': userlist}
    return render(request, 'staff/accountuser/list.html', context)

def createuser(request):
    Cuser = CreateAccountUserForm()
    if request.method == 'POST':
        Cuser = CreateAccountUserForm(request.POST)
        if Cuser.is_valid():
            Cuser.save()
            return redirect('list-user')
    ctx = {'Cuser':Cuser}
    return render(request,'staff/accountuser/user_form.html', ctx)

def infouser(request, pk):
    ures = get_object_or_404(Account, pk=pk)
    form = AccountForm(instance=ures)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=ures)
        if form.is_valid():
            form.save()
            return redirect('list-user')
    context ={
        'user':ures,
        'form':form
    }
    return render(request,'staff/accountuser/infouser.html', context)

def statistical(request):
    return render(request, 'staff/statistical/list.html')

