
# Keywords arguments
def report_product(name, quantity, country = "unknow"):
    print(f'Product: {name}')
    print(f'Quantity: {quantity}')
    print(f'Country: {country}')


# *Args
def calculate_average(*args):
    num_values = len(args)

    if num_values == 0:
        return None
    
    total_sum = sum(args)
    average = total_sum / num_values
    
    return average


def main():
    average_products = calculate_average(121, 250, 96, 15, 5)
    print(average_products)
    print("*" * 40)
    report_product(quantity=200, name="GadgetX", country="Perú")
    print("*" * 40)
    report_product(quantity=400, name="BookX")


if __name__ == '__main__':
    main()