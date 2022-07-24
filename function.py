import re


def ways_to_climb(n, first=0, second=1):
    if n <= 1:
        return first + second
    return ways_to_climb(n - 1, second, first + second)


def path_finder(lst):
    n = len(lst) - 1
    path_sum = 0
    i, j = 0, 0
    while i < n or j < n:
        go_down, go_right = False, False
        path_sum += lst[i][j]
        # Restrict the path if i or j has reached to the limit.
        if i == n:
            go_right = True
        elif j == n:
            go_down = True
        elif lst[i][j + 1] == lst[i + 1][j]:
            # go down
            go_down = True
        elif lst[i][j + 1] > lst[i + 1][j]:
            # go right
            go_right = True
        elif lst[i][j + 1] < lst[i + 1][j]:
            # go down
            go_down = True

        # giving the movement after the successfull decision is made.
        if go_down:
            i += 1

        if go_right:
            j += 1

    # summing up the last value as the while loop end before calculating it.
    return path_sum + lst[i][j]


def can_see_stage(seats):
    col = len(seats[0]) - 1
    row = len(seats) - 1

    for i in range(col):
        for j in range(row):
            if seats[j][i] >= seats[j + 1][i]:
                return False
    return True


def find_pattern(dct_, guess):
    output = []
    for phrase in dct_:
        refined_phrase = dct_[phrase].replace('%d%', '')
        if guess.casefold() in refined_phrase.casefold():
            output.append(f"{phrase}={guess}")
        else:
            output.append(f"{phrase}=None")
    return output


def freed_prisoners(prison):
    if prison[0] == 0:
        return 0
    freed = 0
    opposite_prison = [1 if x == 0 else 0 for x in prison]
    main_prison = prison
    i = 0
    while i < len(main_prison):
        if main_prison[i] == 1:
            freed += 1
            main_prison = opposite_prison if main_prison is prison else prison
        i += 1
    return freed


def advanced_sort(lst: list):
    dct = {}
    for i in lst:
        dct[i] = dct.get(i, 0) + 1

    output = []
    for num in dct.items():
        temp = []
        for i in range(dct[num]):
            temp.append(num)
        output.append(temp)

    return output


def dakti(sentence: str):
    # removing special characters %^&*?><,.
    sentence = re.sub('[^a-zA-Z0-9 -]', '', sentence).strip()
    # sorting the string with respect to the number in the word
    arr = sorted(sentence.split(), key=lambda x: int(
        "".join([n for n in x if n.isdigit()])))
    # array to string
    sentence = " ".join(arr)
    # remove the numbers from the words in sentence
    sentence = re.sub('[^a-zA-Z -]', '', sentence)
    print(sentence)


# Binary search revision.
def binary_search(lst, high, low, x):
    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == x:
            return True
        elif lst[mid] > x:
            return binary_search(lst, mid - 1, low, x)
        else:
            return binary_search(lst, high, mid + 1, x)
    else:
        return False


# lst = [2, 3, 4, 10, 40]
# print(binary_search(lst, len(lst)-1, 0, 9))


def collect(code, n, l=0, r=None, lst=None):
    if lst is None:
        lst = []
        r = n

    # if the string length is not multiple of the n
    # donot add the remaining characters.
    if r > len(code):
        lst.sort()
        return lst

    lst.append(code[l:r])
    return collect(code, n, r, r + n, lst)


def identify(*cube):
    columns = []
    missing = 0
    for part in cube:
        columns.append(len(part))
    rows = len(cube)
    columns.sort()
    columns = columns[::-1]

    max_col = columns[0]
    for i in range(1, len(columns)):
        if max_col - columns[i] != 0:
            missing += max_col - columns[i]

    if missing > 0:
        return f"missing {missing}"

    if rows != max_col:
        return "non-full"

    return "full"


def num_split(num):
    # number is negetive negate the number.
    # split the number
    # number x 10 ** n (n = 0, 1, 2, 3...)
    # the the number to the list
    # return the reverse of the list.
    if not num:
        return [0]

    is_negetive = False
    if num < 0:
        is_negetive = True
        num = -num

    place = 0
    split_list = []
    while num > 0:
        remainder = num % 10
        if is_negetive:
            remainder *= -1
        split_list.append(remainder * (10**place))
        place += 1
        num //= 10

    return split_list[::-1]


def max_product(lst):
    lst.sort()
    l = 0
    r = len(lst) - 1
    max_prod = -10000
    while l < len(lst) - 2:
        for i in range(l + 1, r):
            max_prod = max(max_prod, lst[l] * lst[i] * lst[r])
        l += 1
    return max_prod


def min_product(lst):
    lst.sort()
    lst = lst[::-1]
    l = 0
    r = len(lst) - 1
    min_prod = 100000
    while l < len(lst) - 2:
        for i in range(l + 1, r):
            min_prod = min(min_prod, lst[l] * lst[i] * lst[r])
        l += 1
    return min_prod


def find_and_remove(p_dct):
    # traverse through the list.
    # go to the nested dct
    # check every item'code value for digit or not
    # create a list to contain the items to be removed.
    # when the iteration is over then iterate over the list and delete the item
    # from the dct using the temp dct created.

    for nested_dct in p_dct:
        remove_items = []
        temp = p_dct[nested_dct]
        # print(nested_dct ,temp)
        for item in temp:
            if not temp[item].isdigit():
                remove_items.append(item)
        # print(remove_items)
        for remove_item in remove_items:
            temp.pop(remove_item)

    return p_dct


def connell_sequence(start, end, n):
    # start is the starting row
    # end is the end row
    # n is the number whose index in final list is to be found.
    sequence_start = False
    sequence = []
    num = 1
    # row count
    for row in range(1, end + 1):
        i = 0  # for indexing of each row.

        # for checking if the row is even or not
        even_row = False
        if row % 2 == 0:
            even_row = True
        # to check if the start row is reached ,
        # if reached then start appending the number in the resultant array.
        if row == start:
            sequence_start = True

        while i < row:
            if even_row:
                if num % 2 == 0:  # check if the num is even, according to the row number.
                    if sequence_start:  # if the start is reached then start appending the number.
                        sequence.append(num)
                    i += 1  # incrementing the i only when number is found.
            else:
                if num % 2 != 0:  # check if the num is odd, according to the row number.
                    if sequence_start:  # if the start is reached then start appending the number.
                        sequence.append(num)
                    i += 1  # incrementing the i only when number is found.

            num += 1  # incrementing the num

    # print(sequence)
    if n in sequence:
        return sequence.index(n)
    else:
        return "Not Found!"


#  Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            # var = None
            a[l], a[i] = a[i], a[l]  # backtrack

# Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n)

# def factorial(n):
#     if n == 1:
#         return 1
#     return factorial(n-1) * n

# def permute(a, l, r, output=None):
#     if output is None:
#         output = []

#     if l == r:
#         output.append("".join(a))
#     else:
#         for i in range(l, r):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r, output=output)
#             # a[l], a[i] = a[i], a[l]


#     return output


# string = 'ab'
# array = [_ for _ in string]
# n = len(string)

# print(permute(array, 0, n))


def advanced_sort(lst):
    if len(lst) < 2:
        return [lst]

    lst.sort()
    left = 0
    ans = []
    while left < len(lst) - 1:

        right = left + 1

        while lst[right] == lst[right - 1] and right < len(lst) - 1:
            right += 1

        if right == len(lst) - 1 and lst[right] == lst[right - 1]:
            # if the last element is equal to second last then
            # append all the remaining elements
            ans.append(lst[left:])
            break

        if right == len(lst) - 1 and lst[right] != lst[right - 1]:
            # if the last element is not equal to second last then
            # first append the lst[left->right] and the last remaining element
            ans.append(lst[left:right])
            ans.append([lst[-1]])
            break

        ans.append(lst[left:right])

        left = right

    return ans


def guess_score(code, guess):
    black = 0
    white = 0
    for index, char in enumerate(code):
        if char == guess[index]:
            black += 1
        elif char in guess:
            white += 1

    return {"black": black, "white": white}


print(guess_score("1423", "5678"), {"black": 0, "white": 0})
print(guess_score("1423", "2222"), {"black": 1, "white": 0})
print(guess_score("1423", "1234"), {"black": 1, "white": 3})
print(guess_score("1423", "2211"), {"black": 0, "white": 2})
print(guess_score("2928", "7722"), {"black": 1, "white": 1})
print(guess_score("4845", "6446"), {"black": 1, "white": 1})
