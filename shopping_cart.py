class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
      self.total = 0
      self.employee_discount = employee_discount
      self.items = []
    def add_item(self, name, price, quantity = 1):
        for num in list(range(quantity)):
            self.items.append({"name":name,"price":price})
        self.total += price * quantity
        return self.total
    def mean_item_price(self):
       mean_price = self.total/len(self.items)
       return mean_price
    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        length = len(prices)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]

    def apply_discount(self,discount = None):
        if discount != None:
            percentage = discount/100
            discounted_total = self.total * (1-percentage)
            return discounted_total
        return "No discount applied!"

    def void_last_item(self):
        if len(self.items) > 0:
            self.total -= self.items[-1]["price"]
            self.items.pop()
            return self.total
        return "No items in your cart!"
            

