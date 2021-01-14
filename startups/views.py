from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from django.utils import timezone


def home(request):
    AllCompanies = Company.objects

    return render(request, 'startups/home.html', {'AllCompanies' : AllCompanies})


@login_required(login_url="/accounts/signup")
def CreateProduct(request):

    if request.method == 'POST':
        if request.POST['title'] and request.POST['content'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            NewCompany = Company()

            NewCompany.title = request.POST['title']
            NewCompany.url = request.POST['url']
            NewCompany.Image = request.FILES['image']
            NewCompany.Icon = request.FILES['icon']
            NewCompany.content = request.POST['content']
            NewCompany.publication_date = timezone.datetime.now()
            NewCompany.hunter = request.user
            NewCompany.save()
            
            return redirect('/companies/' + str(NewCompany.id))
        
        else:
            return render(request, 'startups/create.html', {'error' : 'Please fill all the fields'})

    else:
        return render(request, 'startups/create.html')


def FullProductPage(request, company_id):

    ExistingCompany = get_object_or_404(Company, pk=company_id)
    return render(request, 'startups/details.html', {'company' : ExistingCompany})

@login_required(login_url="/accounts/signup")
def upvote(request, company_id):
    if request.method == 'POST':
        ExistingCompany = get_object_or_404(Company, pk=company_id)
        ExistingCompany.Votes += 1
        ExistingCompany.save()

        return redirect('/companies/' + str(ExistingCompany.id))

@login_required(login_url="/accounts/signup")
def upvoteAtHome(request, company_id):
    if request.method == 'POST':
        ExistingCompany = get_object_or_404(Company, pk=company_id)
        ExistingCompany.Votes += 1
        ExistingCompany.save()

        return redirect('home')




