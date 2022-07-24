from function import ways_to_climb
from function import path_finder
from function import can_see_stage
from function import find_pattern
from function import freed_prisoners
from function import advanced_sort
from function import dakti
from function import collect
from function import identify
from function import num_split
from function import max_product
from function import min_product
from function import find_and_remove
from function import connell_sequence

if __name__ == '__main__':
    for i in range(100):
        print(ways_to_climb(i))

    print("*" * 40)

    lst = [
        [1, 0, 3],
        [0, 0, 6],
        [0, 8, 9]
    ]
    lst1 = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 8, 9]
    ]
    print(path_finder(lst))
    print(path_finder(lst1))

    print('*' * 40)

    print(can_see_stage([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(can_see_stage([
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]))
    print(can_see_stage([
        [2, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]))
    print(can_see_stage([
        [1, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]))
    print(can_see_stage([
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 2, 2],
        [5, 5, 5, 5, 4, 4],
        [6, 6, 7, 6, 5, 5]
    ]))
    print(can_see_stage([[1, 2, 3, 2, 1, 1],
                         [2, 4, 4, 3, 2, 2],
                         [5, 5, 5, 10, 4, 4],
                         [6, 6, 7, 6, 5, 5]]))

    print('*' * 40)

    print(find_pattern({
        "Phrase1": "COVID-19 is no good",
        "Phrase2": "COVID-18 is no good",
        "Phrase3": "COVID-17 is no good"
    }, "COVID-19"))
    print(find_pattern({
        "Phrase1": "Edabit is great",
        "Phrase2": "Edabit is very great",
        "Phrase3": "Edabit is really great"
    }, "really")
    )
    print(find_pattern({
        "Phrase1": 'Made in China',
        "Phrase2": 'Made in Brazil',
        "Phrase3": 'Made in America',
        "Phrase4": 'Made in Colombia',

    }, 'Jhonson'))
    print(find_pattern({
        "Phrase1": 'Made12 in China',
        "Phrase2": 'Made in Brazil',
        "Phrase3": '32Made in America',
        "Phrase4": 'Made in Colombia',

    }, 'Made'))

    print('*' * 40)

    print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
    print(freed_prisoners([1, 1, 1]))
    print(freed_prisoners([0, 0, 0]))
    print(freed_prisoners([0, 1, 1, 1]))
    print(freed_prisoners([1, 0, 1, 0, 1, 0]))
    print(freed_prisoners([1, 1, 1, 0, 0, 0]))
    print(freed_prisoners([1, 0, 0, 0, 0, 0, 0]))

    print("*" * 40)

    print(advanced_sort([2, 1, 2, 1]))
    print(advanced_sort([5, 4, 5, 5, 4, 3]))
    print(advanced_sort(["b", "a", "b", "a", "c"]))
    print(advanced_sort([3, 2, 1, 3, 2, 1]))
    print(advanced_sort([5, 5, 4, 3, 4, 4]))
    print(advanced_sort([80, 80, 4, 60, 60, 3]))
    print(advanced_sort(['c', 'c', 'b', 'c', 'b', 1, 1]))
    print(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]))
    print(advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']))

    print("*" * 40)

    dakti("i2s th1s a3 t4est    ")
    dakti("yo2u cr3azy a1re ?  ")
    dakti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves")
    dakti('h4as don2de ah1i n3o ll5egado q7ue 8yo te9-llevare s6abes')

    print('*' * 40)

    str_vector = [
        "intercontinentalisationalism", "strengths", "pneumonoultramicroscopicsilicovolcanoconiosis",
        "lexicographically", "anesthesiologists", "subdermatoglyphic", "sesquipedalianism",
        "recollection", "pseudopseudohypoparathyroidism", "floccinaucinihilipilification",
        "antidisestablishmentarianism", "supercalifragilisticexpialidocious", "incomprehensibilities",
        "astrophysicists", "honorificabilitudinitatibus", "unimaginatively", "euouae", "tsktsk",
        "uncopyrightable"
    ]
    num_vector = [6, 3, 15, 4, 6, 6, 6, 3, 7, 2, 5, 3, 9, 4, 12, 8, 7, 6, 11]
    test_cases = list(zip(str_vector, num_vector))

    for s, n in test_cases:
        print(collect(s, n))

    print('*' * 40)

    print(identify(
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ))
    print(identify(
        ["O", "O"],
        ["O", "O", "O"]
    ))
    print(identify(
        ["O", "O"],
        ["O", "O"],
        ["O", "O", "O"]
    ))

    print(identify(
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"]
    ))
    print(identify(
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O", "O"]
    ))
    print(identify(
        ["O", "O"],
        ["O", "O"]
    ))
    print(identify(
        ["O", "O"],
        ["O"]
    ))

    print("*" * 40)

    print(num_split(39))
    print(num_split(100))
    print(num_split(-434))
    print(num_split(3929))
    print(num_split(10293))
    print(num_split(900))
    print(num_split(-100))

    print("*" * 40)

    print(max_product([1, -1, 1]), -1)
    print(max_product([1, -1, 1, 1]), 1)
    print(max_product([-8, -9, 1, 2, 7]), 504)
    print(max_product([-8, 1, 2, 7, 9]), 126)
    print(max_product([1, 1, 5, 1, 1, -10, -1]), 50)
    print(max_product([-8, -7, -6, -5]), -210)
    print(max_product([-8, -7, -6, -5, 1]), 56)
    print(max_product([1, 0, 1, 0, 0]), 0)
    print(max_product([-5, 1, 10, 0, 0]), 0)
    print(max_product([-5, -1, -1, 0, 0]), 0)
    print(max_product([-5, 1, -1, 0, 0]), 5)
    print(max_product([-5, -3, -1, 0, 4]), 60)
    print(max_product([5, 3, -1, 0, -4, 7, 7, 9]), 441)

    print("*" * 40)

    print(min_product([1, -1, 1]), -1)
    print(min_product([1, -1, 1, 1]), -1)
    print(min_product([-8, -9, 1, 2, 7]), -126)
    print(min_product([-8, 1, 2, 7, 9]), -504)
    print(min_product([1, 1, 5, 1, 1, -10, -1]), -50)
    print(min_product([-8, -7, -6, -5]), -336)
    print(min_product([-8, -7, -6, -5, 1]), -336)
    print(min_product([1, 0, 1, 0, 0]), 0)
    print(min_product([-5, 1, 10, 0, 0]), -50)
    print(min_product([-5, -1, -1, 0, 0]), -5)
    print(min_product([-5, 1, -1, 0, 0]), 0)
    print(min_product([-5, -3, -1, 0, 4]), -15)
    print(min_product([5, 3, -1, 0, -4, 7, 7, 9]), -252)

    print("*" * 40)

    print(find_and_remove({
        "workshop": {
            "bedsheets": "2000",
            "working": "v0g89t7t",
            "pen": "370",
            "movies": "wo1a3d5d",
        },
    }))

print(find_and_remove({
    "bedroom": {
      "slippers": "10000",
      "piano": "5500",
      "call": "vet",
      "travel": "world",
      },
}))

print(find_and_remove({
    'bedroom': {
      'slippers': "10000",
      'piano': "5500",
      'call': "vet",
      'travel': "world",
      },
}))

print(find_and_remove({
    'kitchen': {
      "gold spoons": "900",
      'piano': "550",
      'notes': "ga0r76ba22g4e",
      },
    'cellar': {
        'reminder': "dog",
        'bottle': "750",
    },
}))

print("*" * 40)

print(connell_sequence(1, 3, 4), 2, "Example #1")
print(connell_sequence(2, 3, 4), 1, "Example #2")
print(connell_sequence(4, 5, 22), "Not Found", "Example #3")
print(connell_sequence(1, 1, 1), 0)
print(connell_sequence(1, 1, 0), "Not Found")
print(connell_sequence(1, 100, 100), 54)
print(connell_sequence(4, 5, 77), "Not Found")
print(connell_sequence(11, 22, 300), 103)
print(connell_sequence(30, 32, 974), 67)
print(connell_sequence(13, 88, 300), 80)
print(connell_sequence(1, 1000, 8000), 4044)
print(connell_sequence(111, 1000, 8000), "Not Found")
# print(connell_sequence(10000, 11000, 120999810), 10510404) takes 7-8 seconds

print("*" * 40)

print(advanced_sort([1, 2, 1, 2]), [[1, 1], [2, 2]])
print(advanced_sort([2, 1, 2, 1]), [[2, 2], [1, 1]])
print(advanced_sort([3, 2, 1, 3, 2, 1]), [[3, 3], [2, 2], [1, 1]])
print(advanced_sort([5, 5, 4, 3, 4, 4]), [[5, 5], [4, 4, 4], [3]])
print(advanced_sort([80, 80, 4, 60, 60, 3]), [[80, 80], [4], [60, 60], [3]])
print(advanced_sort(['c', 'c', 'b', 'c', 'b']), [['c', 'c', 'c'], ['b', 'b']])
print(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]),
      [[1234, 1234], [1235, 1235, 1235], [1236]])
print(advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']), [
      ['1234', '1234'], ['1235', '1235', '1235'], ['1236']])
