from django.shortcuts import render

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


def recipe(request, name_recipe):
    servings = request.GET.get('servings')
    if servings:
        my_dict = dict()
        my_dict_temp = dict()
        for ingredient, amount in DATA[name_recipe].items():
            amount_res = amount*int(servings)
            my_dict_temp[ingredient] = amount_res

        my_dict['recipe'] = my_dict_temp
        context = my_dict
    else:
        my_dict = dict()
        my_dict['recipe'] = DATA[name_recipe]
        context = my_dict
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }