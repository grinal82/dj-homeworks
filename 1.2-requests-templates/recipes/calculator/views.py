from django.shortcuts import render, reverse


def home_view(request):
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
