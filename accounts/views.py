from django.contrib.auth.decorators import login_required
from admins.utils import validate_access
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entries
import json


# Create your views here.
@login_required()
def dashboard(request):
    validate_access(request, 'ac')

    # Getting the expenses
    all = Entries.objects.all()
    expenses = all.filter(type=False)

    # Summing all the prices in a category
    exp_tally = {}
    for exp in expenses:
        if exp.cat not in exp_tally:
            exp_tally[exp.cat] = exp.price
        else:
            exp_tally[exp.cat] += exp.price

    # Finding the top 4 categories
    values = exp_tally.items()
    values = sorted(values, reverse=True, key=lambda amt: amt[1])
    if len(values) > 5:
        others = sum([i[1] for i in values[3:]])
        values = values[:4]
        values.append(('others', others))
    exp_tally = dict(values)

    # Summing the income and expenses
    income, expense = 0, 0
    for i in all:
        if i.type:
            income += i.price
        else:
            expense += i.price

    return render(request, 'accounts/dashboard.html', context={"exp_tally": exp_tally,
                                                               "income": income,
                                                               "expense": expense})


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
