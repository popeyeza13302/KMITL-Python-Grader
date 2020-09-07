# week 5
class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.item = []
        else:
            self.item = lst

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.item)

    def deQ(self):
        if self.isEmpty():
            return print(-1)
        return self.item.pop(0)

    def enQ(self, i):
        self.item.append(i)
        return self.item[-1]

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


def checkBlueBomb(lst):
    blueQ = Queue(lst)
    blueBomb = []
    tempQ = Queue()
    kaboom = False

    # check if it less than 3 .. them return and exit
    if blueQ.size() < 3:
        blueBomb.reverse()
        return blueBomb, blueQ.item  # Done and Left

    # 2 Queues .. blueQ and tempQ .. to store deQ and reuse it
    for _ in range(1000):
        # less than 3 in loop ?
        if blueQ.size() < 3:
            for _ in range(blueQ.size()):
                tempQ.enQ(blueQ.deQ())
            else:
                blueQ.item = tempQ.item.copy()
                tempQ = Queue()
                if kaboom is True:
                    kaboom = False
                    continue
                else:
                    break

        # found 3 bombs
        if blueQ.item[0] == blueQ.item[1] == blueQ.item[2]:
            blueQ.deQ()
            blueQ.deQ()
            blueBomb.append(blueQ.deQ())  # add to blue bomb
            kaboom = True
            continue

        # if redQ not empty
        if not blueQ.isEmpty():
            tempQ.enQ(blueQ.deQ())

    blueBomb.reverse()
    return blueBomb, blueQ.item  # Done and Left


def checkRedBomb(lst, blue):
    blueQ = Queue(blue.copy())
    redQ = Queue(lst)
    redBomb = []
    mistake = []
    tempQ = Queue()
    kaboom = False

    # check if it less than 3 .. them return and exit
    if redQ.size() < 3:
        redQ.item.reverse()
        return redBomb, redQ.item, mistake  # Done and Left

    # Insert Ice Bomb to Red team
    # 2 Queues .. redQ and tempQ .. to store deQ and reuse it
    for _ in range(1000):
        # less than 3 in loop ?
        if redQ.size() < 3:
            for _ in range(redQ.size()):
                tempQ.enQ(redQ.deQ())
            else:
                redQ.item = tempQ.item.copy()
                tempQ = Queue()
                if kaboom is True:
                    kaboom = False
                    continue
                else:
                    break

        # found 3 bombs and have more blue to insert
        if redQ.item[0] == redQ.item[1] == redQ.item[2] and not blueQ.isEmpty():
            redQ.item.insert(2, blueQ.deQ())
            if redQ.item[0] == redQ.item[1] == redQ.item[2]:  # check for mistake bombing
                redQ.deQ()
                redQ.deQ()
                mistake.append(redQ.deQ())  # add to mistake
                kaboom = True
                continue

        # if redQ not empty
        if not redQ.isEmpty():
            tempQ.enQ(redQ.deQ())

    # Red Bomb Kaboom Normal
    # 2 Queues .. redQ and tempQ .. to store deQ and reuse it
    for _ in range(1000):
        # less than 3 in loop ?
        if redQ.size() < 3:
            for _ in range(redQ.size()):
                tempQ.enQ(redQ.deQ())
            else:
                redQ.item = tempQ.item.copy()
                tempQ = Queue()
                if kaboom is True:
                    kaboom = False
                    continue
                else:
                    break

        # found 3 bombs
        if redQ.item[0] == redQ.item[1] == redQ.item[2]:
            redQ.deQ()
            redQ.deQ()
            redBomb.append(redQ.deQ())  # add to red bomb
            kaboom = True
            continue

        # if redQ not empty
        if not redQ.isEmpty():
            tempQ.enQ(redQ.deQ())

    redQ.item.reverse()
    return redBomb, redQ.item, mistake  # Done and Left


red, blue = map(list, input('Enter Input (Red, Blue) : ').split())
blueBombDone, blueBombLeft = checkBlueBomb(blue)
redBombDone, redBombLeft, blueMistake = checkRedBomb(red, blueBombDone)

print('Red Team :')
print(len(redBombLeft))
if len(redBombLeft) == 0:
    print('Empty')
else:
    print(''.join(redBombLeft))
print(len(redBombDone), 'Explosive(s) ! ! ! (HEAT)')
if len(blueMistake) > 0:
    print('Blue Team Made (a) Mistake(s)', len(blueMistake), 'Bomb(s)')

print('----------TENETTENET----------')

print('Blue Team :'[::-1])
print(len(blueBombLeft))
if len(blueBombLeft) == 0:
    print('Empty'[::-1])
else:
    print(''.join(blueBombLeft))
print('Explosive)s( ! ! ! )FREEZE('[::-1], len(blueBombDone))
