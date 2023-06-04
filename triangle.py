def check_valid(sides):
    for side in sides:
        if side <=0:
            return False
    if (sides[0]>=(sides[1]+sides[2])) or (sides[1]>=(sides[0]+sides[2])) or (sides[2]>=(sides[0]+sides[1])):
        return False
    return True

def equilateral(sides):
    if not check_valid(sides):
        return False
    if (sides[0]==sides[1]) and (sides[0]==sides[2]):
        return True
    else:
        return False

def isosceles(sides):
    if not check_valid(sides):
        return False
    if (sides[0]==sides[1]) or (sides[1]==sides[2]) or (sides[0]==sides[2]):
        return True
    else:
        return False

def scalene(sides):
    if not check_valid(sides):
        return False
    if (sides[0]!=sides[1]) and (sides[0]!=sides[2]) and (sides[1]!=sides[2]):
        return True
    return False
    
class triangles:
    def __init__(self,sides):
        self.sides = sides
    def check_valid(self):
        sides = self.sides
        for side in sides:
            if side <=0:
                return False
        if (sides[0]>=(sides[1]+sides[2])) or (sides[1]>=(sides[0]+sides[2])) or (sides[2]>=(sides[0]+sides[1])):
            return False
        return True

    def equilateral(self):
        sides = self.sides
        if not self.check_valid():
            return False
        if (sides[0]==sides[1]) and (sides[0]==sides[2]):
            return True
        else:
            return False

    def isosceles(self):
        sides = self.sides
        if not self.check_valid():
            return False
        if (sides[0]==sides[1]) or (sides[1]==sides[2]) or (sides[0]==sides[2]):
            return True
        else:
            return False

    def scalene(self):
        sides = self.sides
        if not self.check_valid():
            return False
        if (sides[0]!=sides[1]) and (sides[0]!=sides[2]) and (sides[1]!=sides[2]):
            return True
        return False
    
