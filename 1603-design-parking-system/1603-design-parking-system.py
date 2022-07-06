class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big 
        self.medium = medium
        self.small = small
        
        self.big_count = 0
        self.med_count = 0
        self.small_count = 0
        

    def addCar(self, carType: int) -> bool:
        if carType == 1: 
            if self.big_count < self.big: 
                self.big_count += 1
                return True
        elif carType == 2:
            if self.med_count < self.medium: 
                self.med_count += 1
                return True
        elif carType == 3:
            if self.small_count < self.small: 
                self.small_count += 1
                return True
        else: 
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)