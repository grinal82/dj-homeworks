from django.shortcuts import render, reverse


def home_view(request):
    """
    Обработчик "Домашней страницы.
    """
    template_name = "calculator/home.html"

    pages = {
        "Рецепт омлета": reverse("omlet"),
        "Рецепт пасты": reverse("pasta"),
        "Рецепт бутерброда": reverse("buter"),
    }

    context = {"pages": pages}
    return render(request, template_name, context)


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    """
    Обработчик ответа при нажатии на "Рецепт омлета".
    Проверяет наличие необезательного параметра в url запросе "servings" (по умолчанию = 1).
    В случае наличия параметра, с помощью request.GET.get забирает значение по ключу 'servings'
    и присваивает в соответствующую переменную.
    Возвращеет render в который передает request, html-шаблон и context.
    Context представляет собой словарь и рецептом омлета: ингредиенты: кол-во (значение из DATA умноженное на переменную 'servings')
    
    """
    servings = int(request.GET.get('servings', 1))
    print()
    print(f'количество блюд = {servings}')
    print()
    recipe = dict()
    result = DATA['omlet']
    for ingredient, amount in result.items():
        recipe[f'{ingredient}'] = round(amount, 2) * servings
    context = {'recipe': recipe}
    print(recipe)

    return render(request, 'calculator/index.html', context)


def pasta(request):
    """
    Обработчик ответа при нажатии на "Рецепт пасты".
    Логика обработчика аналогична def omlet(request)
    """
    servings = int(request.GET.get('servings', 1))
    print()
    print(f'количество блюд = {servings}')
    print()
    recipe = dict()
    result = DATA['pasta']
    for ingredient, amount in result.items():
        recipe[f'{ingredient}'] = float(round(amount, 2)) * servings
    context = {'recipe': recipe}
    print(recipe)

    return render(request, 'calculator/index.html', context)


def buter(request):
    """
    Обработчик ответа при нажатии на "Рецепт бутерброда".
    Логика обработчика аналогична def omlet(request)
    """
    servings = int(request.GET.get('servings', 1))
    print()
    print(f'количество блюд = {servings}')
    print()
    recipe = dict()
    result = DATA['buter']
    for ingredient, amount in result.items():
        recipe[f'{ingredient}'] = round(amount, 2) * servings
    context = {'recipe': recipe}
    print(recipe)

    return render(request, 'calculator/index.html', context)
