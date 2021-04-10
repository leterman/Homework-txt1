import json


def get_shop_list_by_dishes(dishes, person_count):
    lc_dict2buy = {}
    list_ing4dish = {}
    loc_dict_cook_book = read_cook_book()
    for dish in dishes:
        if (dish == '' or dish == ' '):
            continue
        list_ing4dish = loc_dict_cook_book.get(str(dish))   #получен списко ингредиентов для блюда
        for ing in list_ing4dish:
            if ing['ingridient_name'] not in lc_dict2buy.keys():
                lc_dict2buy[ing['ingridient_name']] = {'measure': ing['measure'], 'quantity': 0}
            lc_dict2buy[ing['ingridient_name']]['quantity'] = lc_dict2buy[ing['ingridient_name']]['quantity'] + ( int(ing['quantity'] )) * person_count
    return lc_dict2buy



def get_dishes():
    loc_list = []
    loc_list.append('Запеченный картофель')
    loc_list.append('Омлет')
    return loc_list


def get_persons_num():
    person = int(input('Кол-во человек:'))
    return person


def read_cook_book():
    loc_dict = {}
    lv_dish_name = ''
    lv_ing_num = 0
    lv_ing_proc = 0
    lv_ingredient_line = ''

    with open('dishes_list.txt', 'rt', encoding='UTF8') as cook_book_file:
        for line in cook_book_file:
            lv_dish_name = line.strip()
            list_ing4dish = []
            lv_ing_num = cook_book_file.readline().strip()  # название блюда
            lv_ing_proc = 0
            while (int(lv_ing_num) > lv_ing_proc):
                dict_ing_info = {}
                list_ing_info = []
                lv_ingredient_line = cook_book_file.readline().strip()  # строка с одним ингеридентом
                list_ing_info = lv_ingredient_line.split('|')
                dict_ing_info['ingridient_name'] = list_ing_info[0]
                dict_ing_info['quantity'] = list_ing_info[1]
                dict_ing_info['measure'] = list_ing_info[2]
                list_ing4dish.append(dict_ing_info)
                lv_ing_proc += 1
            loc_dict[str(lv_dish_name)] = list_ing4dish
            cook_book_file.readline()  # пустая строка - просто перещелкиваем
    return loc_dict

def read_cook_book_anc_calc_list():
    loc_dict_cook_book = read_cook_book()
    print('Книга с рецептами:')
    print(json.dumps(loc_dict_cook_book, indent=2, ensure_ascii=False))

    loc_list_dishes = get_dishes()
    loc_persons_num = get_persons_num()

    print('Cписок ингридиентов')
    loc_list2buy = get_shop_list_by_dishes(loc_list_dishes, loc_persons_num)
    print(json.dumps(loc_list2buy, indent=2, ensure_ascii=False))

read_cook_book_anc_calc_list()
