sales_data = {
    "Alice": [
        {"product": "Laptop", "units": 2, "price": 1200},
        {"product": "Mouse", "units": 5, "price": 25}
    ],
    "Bob": [
        {"product": "Monitor", "units": 3, "price": 300},
        {"product": "Keyboard", "units": 4, "price": 45}
    ],
    "Charlie": [
        {"product": "Laptop", "units": 1, "price": 1300},
        {"product": "Mouse", "units": 10, "price": 20}
    ]
}

sales_data_result = {}
units_per_product = {}

for name, revenue in sales_data.items():
    total = sum(product['units'] * product['price'] for product in revenue)
    sales_data_result[name] = total

print("Total revenue per salesperson:")
print(sales_data_result)

top_salesperson = max(sales_data_result, key=sales_data_result.get)
print(f"Top performer was: {top_salesperson} with a revenue of {sales_data_result[top_salesperson]}")
