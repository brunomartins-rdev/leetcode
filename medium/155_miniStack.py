class MinStack:

    def __init__(self):
        self.stack = list()
        self.minValue = list()


    def push(self, val: int) -> None:
        self.stack.append(val)

        # Set minimum value as the value, if that is 
        if self.minValue:
            if self.minValue[-1] >= val:
                self.minValue.append(val)
        else:
            self.minValue.append(val)


    def pop(self) -> None:
        numberToPop = self.stack[-1]
        self.stack.pop()
        if numberToPop == self.minValue[-1]:
            self.minValue.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else False

    def getMin(self) -> int:
        print(f'This is the minimum value stack: {self.minValue}')
        return self.minValue[-1] if self.minValue else False


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.stack)
obj.push(0)
print(obj.stack)
obj.push(1)
print(obj.stack)
obj.push(0)
print(obj.stack)
param_4 = obj.getMin()
print(param_4)
obj.pop()
print(obj.stack)
param_4 = obj.getMin()
print(param_4)
print(obj.stack)
param_3 = obj.top()
print(param_3)
