import copy


def change_list(deg):  # менять лист за шаг, deg = [[4,3,3,2,2]] к примеру
    change_degrees = []

    for l in deg:
        #  1 способ - расписать последнюю
        for i in range(len(l) - 1, 0, -1):
            while i == 1:
                continue
            if l[i] > 1:
                my_copy = copy.deepcopy(l)
                my_copy[i] = my_copy[i] - 1
                if len(l) - 1 == i:
                    my_copy.append(1)
                    break
                else:
                    my_copy[i + 1] += 1
                    break
        my_copy.sort()
        my_copy.reverse()
        good = True
        for el in my_copy:
            if el == -1 or el == 0:
                good = False
                break
        if good:
            change_degrees.append(my_copy)

# 2 способ - уменьшить первую, добавить 1 к последней, если будет не равна уменьшенной
        my_copy2 = copy.deepcopy(l)
        if my_copy2[-1] != my_copy2[0] - 1:
            my_copy2[0] -= 1
            my_copy2[-1] += 1
            my_copy2.sort()
            my_copy2.reverse()
            good = True
            for el in my_copy2:
                if el == -1 or el == 0:
                    good = False
                    break
            if good:
                change_degrees.append(my_copy2)

    result = []
    for el in change_degrees:
        if el not in result:
            result.append(el)
    return result


def main():
    degrees = [4, 3, 3, 2, 2]
    all = [[degrees]]
    i = 0
    while i != 100:
        answer = change_list(all[i])
        cur = []
        for g in answer:
            cur.append(g)
        all.append(cur)
        i += 1
    for str in all:
        print(str)


if __name__ == "__main__":
    main()