def asteroid_collision(asts):
    if len(asts) == 1:
        return asts

    results = asteroid_collision(asts[1:])

    if len(results) > 0 and asts[0] > 0 and results[0] < 0:
        # not normal case (len(results) > 0 for the first case that results size can be 0)

        if asts[0] == abs(results[0]):  # same size .. 2 exploded
            if len(results) > 1:
                return results[1:]  # get the rest back from right
            elif len(results) == 1:
                return []  # nothing left

        elif asts[0] > abs(results[0]):  # left has more than right... right exploded
            return asteroid_collision([asts[0]] + results[1:])

        elif asts[0] < abs(results[0]):  # left has less than right... left exploded
            return results  # right and get the rest back

    else:
        # normal case
        return [asts[0]] + results  # return data back...


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
