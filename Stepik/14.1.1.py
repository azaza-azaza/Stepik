# возвращает стоимость доставки

def get_shipping_cost(quantity):
    how_much = 1000
    for i in range(1,quantity):
        how_much += 120
    return how_much

print(get_shipping_cost(int(input())))