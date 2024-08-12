import pprint

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

products = {}
customers = {}

total = 0
for sale in sales_data:
    # part 1: total revenue
    total += (sale["price"] * sale["quantity"])
    # part 1: product totals
    if sale["product"] in products:
        products[sale["product"]] += sale["quantity"]
    else:
        products[sale["product"]] = sale["quantity"]

    # part 2: customer info
    if sale["customer_id"] in customers:
        customers[sale["customer_id"]] += (sale["price"] * sale["quantity"])
    else:
        customers[sale["customer_id"]] = (sale["price"] * sale["quantity"])

    # part 3: add totals
    sale['total'] = sale["price"] * sale["quantity"]

# print(total)
# print(products)
# print(customers)
# pprint.pprint(sales_data)

# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.
# my_list = [num for num in my_number]

big_sales = [sale for sale in sales_data if sale["total"]>=500]
big_sales.sort(key=lambda x: x["total"], reverse=True)
# print(big_sales)

number_of_sales = {}
loyal_customers = []
for sale in sales_data:
    if sale["customer_id"] in number_of_sales:
        number_of_sales[sale["customer_id"]] += 1
    else:
        number_of_sales[sale["customer_id"]] = 1
    
for customer in number_of_sales.keys():
    if number_of_sales[customer] >= 2:
        loyal_customers.append(customer)
    
print(loyal_customers)