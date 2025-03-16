def apply_sorting_network(l, network):
    """
    Applies a sorting network to the input list.

    Parameters:
        l (list): The list of comparable items to sort.
        network (list of list of tuples): A sorting network where each inner list
            represents a layer of compare-exchange (CE) operations. Each tuple (i, j) with i < j
            indicates that elements at index i and j should be compared and swapped if l[i] > l[j].

    Returns:
        list: A new list after the network is applied.
            Assuming the network is a valid sorting network, then the list will be sorted.
    """

    sorted_lst = l.copy()

    for layer in network:
        for i, j in layer:
            if sorted_lst[i] > sorted_lst[j]:
                sorted_lst[i], sorted_lst[j] = sorted_lst[j], sorted_lst[i]
    return sorted_lst



if __name__ == "__main__":

    # see https://bertdobbelaere.github.io/sorting_networks.html#N4L5D3
    test_network = [
        [(0, 2), (1, 3)],
        [(0, 1), (2, 3)],
        [(1, 2)]
    ]
    test_list = [3, 1, 4, 2]

    result = apply_sorting_network(test_list, test_network)
    print("Input:", test_list)
    print("Sorted:", result)