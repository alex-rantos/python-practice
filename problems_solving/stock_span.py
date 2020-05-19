"""Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6]."""

class StockSpanner:

    def __init__(self):
        self.st = []
        self.i = 0
        
    """
    Keep all elements in decreasing order in stack and keep track of how many elements you have proccessed (@self.i)
    While the top of the stack is less than the current price pop the top 
    and then return the current index (self.i) minus the index of the top of the stack which is an element greater than price.
    if Stack contains no elements the current price is the highest so return current index(@self.i)
    """
    def next(self, price: int) -> int:
        self.i += 1
        
        while (len(self.st) - 1 >= 0 and self.st[-1][0] <= price):
            self.st.pop()
        
        self.st.append((price,self.i))
        
        if (len(self.st) == 1):
            return self.i
        else:
            return self.i - self.st[-2][1]  
            
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)