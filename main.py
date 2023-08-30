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


    def get_shop_list_by_dishes(person_count, dishes):
        for dish in dishes:
            if dish in cook_book:
                for ingredients in cook_book[dish]:
                    product = ingredients['product']
                    quantity = int(ingredients['quantity']) * int(person_count)
                    measure = ingredients['measure']
                    print(product, quantity, measure)


    get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])


