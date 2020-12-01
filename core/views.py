from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, "index.html", {'tabs': request.path.split('/')})


def not_found(request, resource):
    return render(request, "misc/404.html")


def one(request):
    if request.method == "POST":
        if request.POST['password'].lower() == 'na gorshke sidel korol':
            response = {
                "text": "<p class='h1'>Отличная работа, Фасолинка!</p>"
                        "<p class='h3 text-muted'>Теперь мы знаем чем занимается их руководство.</p>",
                "button": f"<a href='{reverse('two')}' style='text-decoration: none'><button class='btn "
                          f"btn-block btn-success'>Перейти к следующему заданию</button></a>"
            }
            return JsonResponse(response)
        return HttpResponse(status=400)
    return render(request, "one.html")


def two(request):
    if request.method == "POST":
        if request.POST['answer'] == '31415926':
            response = {
                "text": "<p class='h1'>А ты неплохо справляешься!</p>"
                        "<p class='h3 text-muted'>Задача не из простых, но а кому сейчас легко.</p>",
                "button": f"<a href='{reverse('three')}' style='text-decoration: none'><button class='btn "
                          f"btn-block btn-success'>Перейти к следующему заданию</button></a>"
            }
            return JsonResponse(response)
        return HttpResponse(status=400)
    return render(request, "two.html")


def three(request):
    if request.method == "POST":
        if request.POST['answer'].lower() == 'fisher college':
            response = {
                "text": "<p class='h1'>Ты просто чудо!</p>"
                        "<p class='h3 text-muted'>С тобой мы покорим весь мир.</p>",
                "button": f"<a href='{reverse('four')}' style='text-decoration: none'><button class='btn "
                          f"btn-block btn-success'>Перейти к следующему заданию</button></a>"
            }
            return JsonResponse(response)
        return HttpResponse(status=400)
    return render(request, "three.html")


def four(request):
    if request.method == "POST":
        if request.POST['answer'].lower() == 'bridge':
            response = {
                "text": "<p class='h1'>Прекрасно!</p>"
                        "<p class='h3 text-muted'>Мы уже устанавливаем наблюдение за местом.</p>",
                "button": f"<a href='{reverse('five')}' style='text-decoration: none'><button class='btn "
                          f"btn-block btn-success'>Перейти к следующему заданию</button></a>"
            }
            return JsonResponse(response)
        return HttpResponse(status=400)
    return render(request, "four.html")


def five(request):
    if request.method == "POST":
        if request.POST['answer'].lower() == 'bandit':
            response = {
                "text": "<p class='h1'>Ой-ой-ой-ой-ой!</p>"
                        "<p class='h3 text-muted'>Ты заменяешь нам целый отдел! Я лично передам дополнительную "
                        "награду</p>",
                "button": f"<a href='{reverse('six')}' style='text-decoration: none'><button class='btn "
                          f"btn-block btn-success'>Перейти к следующему заданию</button></a>"
            }
            return JsonResponse(response)
        return HttpResponse(status=400)
    return render(request, "five.html")


def six(request):
    return render(request, "six.html")


def seven(request):
    return render(request, "seven.html")


def eight(request):
    return render(request, "eight.html")
