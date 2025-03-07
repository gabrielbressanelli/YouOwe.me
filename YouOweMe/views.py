from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DeadBeatForm, DebtForm
from django.contrib import messages
from .models import DeadBeat, Debt
from itertools import cycle


def index_view(request):
    all_deadbeats = DeadBeat.objects.all()
    form = DeadBeatForm(request.POST or None)


    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Boa mlk, finalmente pagou os cria!')
        else:
            messages.warning(request, 'Insert a valid debt id!')

        return render(request, 'index.html', {'all':all_deadbeats} )

    
    return render(request, 'index.html', {'all':all_deadbeats} )


#def table(request):
#    all_deadbeats = DeadBeat.objects.all
#    return render(request, 'table.html', {'all':all_deadbeats} )

def debt(request):
    all_debts = Debt.objects.all()
    if request.method == "POST":
        form = DebtForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'Vagabundo, criou mais uma dívida!')
        return render(request, 'debt.html', {'all_debts':all_debts})
    else:
        return render(request, 'debt.html', {'all_debts':all_debts})


def total_paid(request):
    # fetching Debt from model.py
    debts = Debt.objects.all()
    
    # dictionary to save the total amount paid for each debt 
    total_paid_per_debt = []

    # image link dictionary list
    image_links = [
        {"image_url":"https://i.pinimg.com/736x/27/2b/eb/272beb84bfb4ad65f6368080e0a20b9d.jpg"},
        {"image_url":"https://www.criarmeme.com.br/meme/meme-60488-LOGO-VOCE-QUERER-FALAR-DE-POLITICO-CORRUPTO-LOGO-VOCE-QUE-E-CALOTEIRO.jpg"},
        {"image_url":"https://live.staticflickr.com/7390/12675181334_9df549a180_z.jpg"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7lW3c1sGn-MXfwRVIjnfXEcDb1SYsGZJm_A&s"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKjMuyi3f1UdteAk-O9A8tUJImSvhCUkU61g&s"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEDV12GBkIDbqXTD4Ya_9zj1-nK54xHKz8BA&s"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNmplvi9fq2rPFGJwMmot-8xjjI5KV9H43Dg&s"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNGi1l-wBK49uYSyAsigdIG1zn1HYh9OkRGRpq6u98NfN5eiavIF_mX5EeE2oczIcp9dQ&usqp=CAU"},
        {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZJXEUaX1iL4HIJYo6IiKRLDVvYfRsC3cjCQ&s"},
        {"image_url":"https://preview.redd.it/dke2bwp4wl871.jpg?auto=webp&s=c297cf5f30bd96285bcaeced4c73e991eb5a593b"},
    ]

    # If number of debts is bigger thant the amount of images, it will repeat images 
    image_cycle = cycle(image_links)

    # looping through each debt 
    for debt in debts:
        # fetching all the payments by specific deadbeat
        payments_for_debt = DeadBeat.objects.filter(debt=debt)

        # sum up all the payments
        total_amount = sum(payment.amount for payment in payments_for_debt)

        # storing each total aomunt by id in the dictionary
        total_paid_per_debt.append({
            'id': debt.id,
            'name': debt.name,  # Adjust if it's named differently in your model
            'total_paid': total_amount,
            'total_owned': (debt.total_amount - total_amount)
        })

        # zipping both lists together to pass them
        debt_with_images = zip(total_paid_per_debt, image_cycle)

    return render(request, 'total_paid.html', {
        'debt_with_images':debt_with_images
        })






  