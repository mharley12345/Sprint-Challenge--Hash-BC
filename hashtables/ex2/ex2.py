#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # let store all tickets in hashtable
    for each_ticket in tickets:
        hash_table_insert(hashtable, each_ticket.source,
                          each_ticket.destination)

    # we know starting location has source of NONE, so we can store the respective destination in the route
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # Now loop through the rest and order them according their sources
    # Skip one in length as we already added first destination
    # Use previous desintation as lookup for next following destination
    for index in range(1, length):
        route[index] = hash_table_retrieve(hashtable, route[index-1])

    return route[:-1]