#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # item weights
    # limit = item1 weight + item2 weight
    # return tuple
    #store each wieght as a key in the hashtable
    #store index of each wieght as it is value
    for index, value in enumerate (weights):
        hash_table_insert(ht, value, index)
    for index, weight in enumerate(weights):
        difference = limit - weight
        if hash_table_retrieve(ht, difference) is not None:
            value = hash_table_retrieve(ht, difference)
            if value >= index:
                return [value, index]
            else:
                return [index, value]
    """
    YOUR CODE HERE
    """
    return None

# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]   since these are the indices of weights 15 and 6 whose sum equals 21

# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")


# weights_1 = [9]
# answer_1 = get_indices_of_item_weights(weights_1, 1, 9)


# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)


# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)


# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# get_indices_of_item_weights(weights_4, 9, 7)

# answer_4[0] == 6
# answer_4[1] == 2

