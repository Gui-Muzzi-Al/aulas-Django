from django.shortcuts import render


def blog(request):
    print("blog")

    context = {
        "text": "Olá Blog",
        "title": "Essa é a pagina do blog - ",
    }

    return render(request, "blog/index.html", context)


def exemplo(request):
    print("exemplo")

    context = {
        "text": "Olá Exemplo",
        "title": "Essa é a pagina do exemplo - ",
    }

    return render(request, "blog/exemplo.html", context)
