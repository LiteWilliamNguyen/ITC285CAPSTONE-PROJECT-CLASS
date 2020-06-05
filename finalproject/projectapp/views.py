from django.shortcuts import render, get_object_or_404
from .models import Product, Monk, Member
from .forms import ProductForm, MonkForm, MemberForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'projectapp/index.html')

def getProduct(request):
    med_list=Product.objects.all()
    context={'product_list' : product_list}
    return render(request,'projectapp/product.html', context=context)

def getMonk(request):
    monk_list=Monk.objects.all()
    context={'monk_list' : monk_list}
    return render(request, 'projectapp/monk.html', context=context)

def getMember(request):
    member_list=Member.objects.all()
    context={'member_list' : member_list}
    return render(request, 'projectapp/member.html', context=context)


def newProduct(request):
    form=ProductForm
    if request.method =='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()
    return render(request, 'projectapp/newproduct.html', {'form': form})
@login_required
def newMonk(request):
    form=MonkForm
    if request.method =='POST':
        form=MonkForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MonkForm()
    else:
        form=MonkForm()
    return render(request, 'projectapp/newmonk.html', {'form': form})
@login_required
def newMember(request):
    form=MemberForm
    if request.method =='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MemberForm()
    else:
        form=MemberForm()
    return render(request, 'projectapp/newmember.html', {'form': form})



def loginMessage(request):
    return render(request, 'projectapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'projectapp/logoutmessage.html')