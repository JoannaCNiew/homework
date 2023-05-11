from django.shortcuts import render
import random


def random_view(request):
    THOUGHT_LIST = [
        "Budząc się rano, pomyśl jaki to wspaniały skarb żyć, oddychać i móc się radować.",
        "Dopóki żyjesz, dopóki można, bądź dobry.",
        "Najważniejsza jest prostota.",
        "Nie należy się gniewać na bieg wypadków, bo to ich nic nie obchodzi.",
        "Polub twoją pracę, nawet gdyby była mało znacząca i odpoczywaj przy niej.",
        "Trzeba ludzi znosić, jeśli nie umie się ich poprawić.",
    ]
    return render(
        request,
        'random_app/thought.html',
        context={
            'thoughts': random.choice(THOUGHT_LIST),
        }
    )