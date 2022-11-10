def check_valid(sides):
    for side in sides:
        if side <=0:
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
    if not equilateral(sides):
        if (sides[0]==sides[1]) or (sides[1]==sides[2]) or (sides[0]==sides[2]):
            return True
        else:
            return False
    return False

def scalene(sides):
    if not check_valid(sides):
        return False
    if (sides[0]!=sides[1]) and (sides[0]!=sides[2]) and (sides[1]!=sides[2]):
        return True
    return False
    
