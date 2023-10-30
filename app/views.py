from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def Hello_Friend(request:HttpRequest, name: str) -> HttpResponse:
    hey = f"Hey, {name}!"
    return HttpResponse(hey)


def How_Old(request:HttpRequest, end: int, birthyear: int) -> HttpResponse:
    age = end - birthyear
    return HttpResponse(age)


def order(request:HttpRequest, burgers:int, fries:int, drinks:int) -> HttpResponse:
    burger_price = 4.50
    fries_price = 1.5
    drinks_price = 1
    burger_total = burgers * burger_price
    fries_total = fries * fries_price
    drinks_total = drinks * drinks_price
    total = burger_total + fries_total + drinks_total
    return HttpResponse(total)
