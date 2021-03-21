from django.shortcuts import render

def main(request):
    return render(request, "main.html")


def hello(request):
    userName = request.GET['name']
    return render(request, "hello.html",{'userName':userName})