from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/home.html'
    
    pages = {
        'Омлет (omlet)': reverse('omlet'),
        'Паста (pasta)': reverse('pasta'),
        'Бутерброд (buter)': reverse('buter')
    }
    
    context = {
        'pages': pages
    }
    print(context)
    return render(request, template_name, context)

def recipes(request, name):
    template_name = 'calculator/index.html'
    person_count = int(request.GET.get('servings', 1))
    recipe_dict = {}
    for key, value in DATA[name].items():
        recipe_dict[key] = round(value * person_count, 2)

    context = {
        'name' : name.upper(),
        'recipe': recipe_dict,
        'person_count': person_count,
        'home': reverse('home')
    }
    return render(request, template_name, context)

def omlet(request):
    return recipes(request, 'omlet')

def pasta(request):
    return recipes(request, 'pasta')

def buter(request):
    return recipes(request, 'buter')