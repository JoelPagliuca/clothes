def sum_of_clothes(temp, jackets, pulovers, shirts):
    sums = -100
    jacket = None
    pul = None
    shirt = None

    for i in range(len(jackets)):
        for j in range(len(pulovers)):
            for k in range(len(shirts)):
                if 'points' in dir(jackets[0]):
                    first = jackets[i].points
                else:
                    first = 0
                if 'points' in dir(pulovers[0]):
                    second = pulovers[j].points
                else:
                    second = 0
                if 'points' in dir(shirts[0]):
                    third = shirts[k].points
                else:
                    third = 0
                fst = first + second + third
                if abs(fst - temp) < abs(sums-temp):
                    sums = fst
                    jacket = jackets[i]
                    pul = pulovers[j]
                    shirt = shirts[k]
                st = second+third
                if abs(st - temp) < abs(sums-temp):
                    sums = st
                    jacket = None
                    pul = pulovers[j]
                    shirt = shirts[k]
                ft = first + third
                if abs(ft - temp) < abs(sums - temp):
                    sums = ft
                    jacket = jackets[i]
                    pul = None
                    shirt = shirts[k]
                t = third
                if abs(t - temp) < abs(sums - temp):
                    sums = t
                    jacket = None
                    pul = None
                    shirt = shirts[k]

    return jacket, pul, shirt


def nearest(categorie, new_temp, underwear):
    difference = -100
    near = None
    for item in categorie:
        if new_temp < 40 and underwear and item.kind == 'болоники' or new_temp < 32 and item.kind == 'болоники':
            continue
        if abs(item.points - new_temp) < abs(difference):
            near = item
            difference = abs(item.points - new_temp)

    return near


def func(temp, clothes):
    temp = -temp+25
    categories = {}
    total = []
    for item in clothes:
        if item.clothes_type not in categories:
            categories[item.clothes_type] = []
            categories[item.clothes_type].append(item)
        else:
            categories[item.clothes_type].append(item)

    if 'pullover' not in categories:
        categories['pullover'] = [None]
    if 'shirt' not in categories:
        categories['shirt'] = [None]
    if 'jacket' not in categories:
        categories['jacket'] = [None]

    up = sum_of_clothes(temp, categories['jacket'], categories['pullover'], categories['shirt'])

    underwear = False
    for categorie in categories:

        if 32 < temp < 40 and categorie == 'pants':
            for item in categories[categorie]:
                if item.kind in ['подштаники', 'термобельё'] and not underwear:
                    total.append(item)
                    underwear = True
        if categorie not in ['pullover', 'shirt', 'jacket']:
            total.append(nearest(categories[categorie], temp, underwear))

    total.extend(list(up))
    return total

