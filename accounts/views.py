from django.contrib.auth.decorators import login_required
from admins.utils import validate_access
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entries
from .utils import *
import json


# Create your views here.
@login_required()
def dashboard(request):
    validate_access(request, 'ac')

    # Getting the expenses
    all = Entries.objects.all()
    expenses = all.filter(type=False)
    incomes = all.filter(type=True)

    # Summing all the prices in a category
    exp_tally = sum_and_order(expenses)
    inc_tally = sum_and_order(incomes)
    print(exp_tally)
    print(inc_tally)

    # Summing the income and expenses
    income, expense = 0, 0
    for i in all:
        if i.type:
            income += i.price
        else:
            expense += i.price

    netprofit = income - expense

    return render(request, 'accounts/dashboard.html', context={"exp_tally": exp_tally, "inc_tally": inc_tally,
                                                               "income": income, "expense": expense, "netprofit": netprofit})


@login_required()
def entries(request):
    validate_access(request, 'ac')

    # Handling the request to save entries
    if 'entries' in request.GET:
        data = json.loads(request.GET['entries'])
        for ent in data.values():
            t = ent[3] == 'Income'
            entry = Entries(date=ent[0], desc=ent[1], cat=ent[2], type=t, price=int(ent[4]))
            entry.save()
        return HttpResponse('success')

    # getting all the entries and the unique categories
    entries = Entries.objects.all()
    cats = []
    for cat in entries.values('cat').distinct():
        cats.append(cat['cat'])

    return render(request, 'accounts/entries.html', context={"entries": entries, "cats": cats})
