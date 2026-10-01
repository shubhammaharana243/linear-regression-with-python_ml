def find_average(data):
    total = 0

    for value in data:
        total += value

    return total / len(data)


def find_deviation(data, mean):
    deviations = []

    for value in data:
        deviations.append(value - mean)

    return deviations


def find_squared_deviation(data):
    squared = []

    for value in data:
        squared.append(value ** 2)

    return squared


def find_product_of_deviation(data1, data2):
    products = []

    for i in range(len(data1)):
        products.append(data1[i] * data2[i])

    return products
while True:
    try:
        x = list(map(float, input("Enter x values data: ").split()))
        y = list(map(float, input("Enter y values data: ").split()))

    except ValueError:
        print("\nError! Enter data like:- 1 2 3 4 5\n")

    else:    
        if len(x) != len(y):
            print("\nError: x and y must have the same number of values.\n")
        else:
            input_x = int(input("\nEnter x to find y: "))

            x_mean = find_average(x)
            y_mean = find_average(y)

            x_deviation = find_deviation(x, x_mean)
            y_deviation = find_deviation(y, y_mean)

            squared_x_deviation = find_squared_deviation(x_deviation)

            product_of_deviation = find_product_of_deviation(x_deviation, y_deviation)

            slope = sum(product_of_deviation) / sum(squared_x_deviation)

            intercept = y_mean - slope * x_mean

            predicted_y = intercept + slope * input_x

            print(f"\nPredicted y: {predicted_y}")

            break
