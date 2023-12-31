def get_cook_book():
    cook_book = {}
    with open('files/recipes.txt', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            dict_ingredients = []
            list_ingredients = {}
            people_count = file.readline()
            for i in range(int(people_count)):
                files_line = file.readline()
                product, quantity, measure = files_line.strip().split(' | ')
                dict_ingredients.append({'product': product, 'quantity': quantity, 'measure': measure})
                dep = {dish_name: dict_ingredients}
            blank_line = file.readline()
            cook_book.update(dep)
    return cook_book

def get_shop_list_by_dishes(person_count, dishes, cook_book):
    shop_list = []
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                product = ingredients['product']
                quantity = int(ingredients['quantity']) * int(person_count)
                measure = ingredients['measure']
                shop_list.append([product, measure, quantity])
    shop_dict = {}
    measure_dict = {}
    for product, measure, quantity in shop_list:
        measure_dict[product] = measure
        shop_dict[product] = shop_dict.get(product, 0) + quantity

    shop_dict_final = {}
    for item in shop_dict.items():
        shop_dict_final[item[0]] = {'measure': measure_dict.get(item[0]), 'quantity': item[1]}

    print(shop_dict_final)

cook_book = get_cook_book()
get_shop_list_by_dishes(2, ['Омлет', 'Омлет'], cook_book)
