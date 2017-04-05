def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    bus_capacity = 50

    # calculating number of needed buses
    if n % bus_capacity == 0:
        return int(n / bus_capacity)
    else:
        return int((n / bus_capacity) + 1)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    gains = 0
    losses = 0

    for i in price_changes:
        if i >= 0:
            # calculate sum of the gains
            gains += i
        else:
            # calculate sum of the losses 
            losses += i
            
    return (gains, losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    # lets recognize first, middle and end items of the list L
    first = L[0:k]
    middle = L[k:-k]
    end = L[-k:]
    # final list
    L[:] = end + middle + first


if __name__ == '__main__':
    import doctest
    doctest.testmod()

