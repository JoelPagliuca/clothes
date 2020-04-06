def nearest(categorie, new_temp):
    difference = 9
    near = None
    for item in categorie:
        print(item)
        if abs(item.points - new_temp) < difference:
            near = item
            difference = abs(item.points - difference)

    if difference > 2:
        near.message = 'сомнительно'
    else:
        near.message = None
    return near


def func(temp, clothes):
    temp = -temp+25
    new_temp = temp/6
    print(new_temp)
    categories = {}
    total = []
    for item in clothes:
        if item.clothes_type not in categories:
            categories[item.clothes_type] = []
            categories[item.clothes_type].append(item)
        else:
            categories[item.clothes_type].append(item)

    for categorie in categories:
        if temp > 32 and categorie == 'pants':
            for item in categories[categorie]:
                if item.kind in ['подштаники', 'термобельё']:
                    total.append(item)
            continue
        total.append(nearest(categories[categorie], new_temp))

    return total

