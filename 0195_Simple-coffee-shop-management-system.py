# The Konditorie coffee shop sells coffee at $10.50 a pound plus the cost od shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a program that calculates the cost of an order.


coffee_price_per_pound = 10.50
shipping_rate_per_pound = 0.86
Fixed_overhead_per_pound = 1.50

pound = int(input("Enter the number of pounds : "))

coffee_price = coffee_price_per_pound * pound
shipping_price = (shipping_rate_per_pound * pound) + Fixed_overhead_per_pound
total = coffee_price + shipping_price

print(f"Coffee Cost : ${coffee_price}")
print(f"Shipping Cost : ${shipping_price}")
print(f"Total Cost : ${total}")
