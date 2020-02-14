#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)





def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Look the length of weights given

    for index in range(length):

        # compare the difference between the limit and each weight given
        diff = limit - weights[index]

        # Check the table before newer weights added, otherwise proceed adding more weights to hashtable

        # Find the indices of weights that hit the limit
        target = hash_table_retrieve(ht, diff)

        # If target is not empty, then index of other element needed to sum up to limit is found
        if target is not None:
            # sum of Index weight and target weight should hit the limit
            return (index, target)
        # Store the weights inside of a hashtable
        hash_table_insert(ht, weights[index], index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
