import re

directions = ["N","W","S","E"]


def checkCoordinateFormat(coordinate):
    splittedCoordinate = coordinate.split(" ")
    if(len(coordinate) != 5 or len(splittedCoordinate) != 3):
        return False,"You entered data in the wrong format. You must enter data in 'X Y D' format (X coordinate, Y coordinate, Direction)"
    if(not splittedCoordinate[0].isdigit() or not splittedCoordinate[1].isdigit()):
        return False,"Coordinates must be an integer"
    if(not splittedCoordinate[2].upper() in directions):
        return False, "Direction not found. Acceptible directions are 'N,S,W,E'"
    return True, "Succeded"

def checkMoveFormat(moveArray):
    pattern = re.compile('^[LMRlmr]+$')
    if(not re.search(pattern, moveArray)):
        return False, "You entered data in the wrong format. Entered directions must be L, M or R"
    return True, "Succeded"


def move(coordinate,moveArray):
    splittedCoordinate = coordinate.split(" ")
    roverX = int(splittedCoordinate[0])
    roverY = int(splittedCoordinate[1])
    roverD = splittedCoordinate[2].upper()
    upperMoveArray = moveArray.upper()
    for moveLetter in upperMoveArray:
        if moveLetter == 'L':
            if roverD == 'E':
                roverD = 'N'
            else:
                roverD = directions[directions.index(roverD)+1]
        elif moveLetter == 'R':
            if roverD == 'N':
                roverD = 'E'
            else:
                roverD = directions[directions.index(roverD)-1]
        elif moveLetter == 'M':
            if roverD == 'N':
                roverY += 1
            elif roverD == 'S':
                roverY -= 1
            elif roverD == 'W':
                roverX -= 1
            elif roverD == 'E':
                roverX += 1
    return str(roverX) + " " + str(roverY) + " " + roverD

print('rover count:')
roverCount = input()
for i in range(int(roverCount)):
    print('Enter Rover '+ str(i+1) + ' coordinate(eg. 0 2 N):')
    isCorrect=False
    while(isCorrect == False):
        coordinate = input()
        checkedCoordinateResult,checkedCoordinateError = checkCoordinateFormat(coordinate)
        if(checkedCoordinateResult == True):
            while(isCorrect == False):
                print('Enter the moves you want to make(eg. LRMRRMLLR):')
                moveArray = input()
                checkedMoveResult,checkedMoveError = checkMoveFormat(moveArray)
                if(checkedMoveResult == True):
                    result = move(coordinate,moveArray)
                    print("Last Coordinate for Rover "+str(i+1)+ " = " + result)
                    isCorrect=True
                else:
                    print(checkedMoveError)
        else:
            print(checkedCoordinateError)


