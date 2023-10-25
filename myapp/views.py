from django.shortcuts import render


def my_menu_page(request):
    context = {
        'page_title': 'Моя страница с меню',
    }
    return render(request, 'myapp/menu_template.html', context)
