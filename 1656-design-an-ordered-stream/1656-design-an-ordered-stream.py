class OrderedStream:

    def __init__(self, n: int):
        self.output = [None] * n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.output[idKey-1] = value
        
        
        result = []
        
        while self.pointer < len(self.output) and self.output[self.pointer] is not None:
                result.append(self.output[self.pointer])
                self.pointer += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)