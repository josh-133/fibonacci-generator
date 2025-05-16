class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.count += 1
            self.a, self.b = self.b, self.a + self.b
            return self.b
        
if __name__ == "__main__":    
    fib = Fibonacci(10)

    for num in fib:
        print(num)
    