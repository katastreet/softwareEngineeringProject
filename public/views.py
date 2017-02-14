from django.shortcuts import render
from django.views import generic
from django.db.models.functions import Lower
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .models import OfficeData
from forms import OfficeForm


# Create your views here.
class Indexview(generic.TemplateView):
    template_name = "public/index.html"


def loginView(request):
    if request.user.username != '':
        return HttpResponseRedirect(reverse('public:publicmain'))
    error = request.GET.get('error')
    if error == 'incorrect':
        context = {'loginerror': 'incorrect username or password', }
    else:
        context = {}
    return render(request, 'public/login.html', context)


def authenticateView(request):
    #  if request.POST only used then we get exception error if not found. get allows to set default value
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    #  authenticate object is provided default by django
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('public:publicmain'))
    else:
        return HttpResponseRedirect("%s?%s" % (reverse('public:login'), "error=incorrect"))


def logoutView(request):
    if request.user.username is not None:
        auth.logout(request)

    return HttpResponseRedirect(reverse('public:index'))


def invalidLoginView(request):
    return HttpResponse('invalid login page')


def validLoginView(request):
    return HttpResponse('valid login page')


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('public:login'))
        else:
            return render(request, 'public/signup.html', {'form': form})

    context = {}
    context['form'] = UserCreationForm()
    return render(request, 'public/signup.html', context)


def publicmainView(request):
    username = request.user.username
    data = request.user.publicuserdata_set.all()

    finaldata = [OfficeData.objects.get(productName=dat.productName, modelNo=dat.modelNo) for dat in data]

    if username == '':
        return HttpResponseRedirect(reverse('public:login'))
    else:
        return render(request, 'public/publicmain.html', {'username': username, 'data': finaldata})


def searchView(request):
    if request.method == 'GET':
        searchText = request.GET.get('search', '')  # search text
        searchCatagory = request.GET.get('catagory', '')  # search catagory:agriculture,etc
        searchSelectBy = request.GET.get('by', '')  # search filter i.e a-z, by date,etc

        #  return render(request, 'public/ajaxSearch.html', {'search': searchText, 'catagory': searchCatagory, 'by': searchSelectBy, })

        relevant_data = OfficeData.objects.filter(productName__contains=searchText, leasable=True) | OfficeData.objects.filter(productName__contains=searchText, canBeBought=True)

        if searchCatagory != '':
            relevant_data = relevant_data.filter(product_type=searchCatagory)

        if searchSelectBy == 'A':
            relevant_data = relevant_data.order_by(Lower('productName'))
        elif searchSelectBy == 'D':
            relevant_data = relevant_data.order_by('-modelDate')
        elif searchSelectBy == 'P':
            relevant_data = relevant_data.order_by('boughtprice')

        return render(request, 'public/ajaxSearch.html', {'data': relevant_data, })


def officeDataView(request):
    if request.POST:
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            #  http redirect
    else:
        form = OfficeForm()
        #  do same as before as for signup
