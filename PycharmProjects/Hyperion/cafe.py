menu = ['espresso', 'double espresso', 'flat white', 'cappuccino']  # creating menu list
stock = {'espresso': 10, 'double espresso': 5, 'flat white': 8, 'cappuccino': 3}  # creating stock dictionary
price = {'espresso': 1.2, 'double espresso': 2, 'flat white': 2.4, 'cappuccino': 2.5}  # creating prices dictionary
sum = 0  # variable to store a sum of the stock value
for a in stock.items():  # loop to check each line of stock
    for i in price.items():  # loop to checl each line of price
        if a[0] == i[0]:  # if the key of the stock is equal key of price
            sum += a[1] * i[1]  # multiply value of the stock with value of the price and add to the sum

print(f'Total stock worth = {sum}')  # return sum of each multiplication

