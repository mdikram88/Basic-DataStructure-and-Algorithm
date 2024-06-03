binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(ind):
    return 2 * ind + 1

def right_child_index(ind):
    return 2 * ind + 2

def pre_order(ind):
    if ind >= len(binary_tree_array) or binary_tree_array[ind] is None:
        return []
        
    return [binary_tree_array[ind]] + pre_order(left_child_index(ind)) + pre_order(right_child_index(ind))

def in_order(ind):
    if ind >= len(binary_tree_array) or binary_tree_array[ind] is None:
        return []

    return in_order(left_child_index(ind)) + [binary_tree_array[ind]] + in_order(right_child_index(ind))

def post_order(ind):
    if ind >= len(binary_tree_array) or binary_tree_array[ind] is None:
        return []
    return post_order(left_child_index(ind)) + post_order(right_child_index(ind)) + [binary_tree_array[ind]]


print("Pre-order Traversal:", pre_order(0))
print("In-order Traversal:", in_order(0))
print("Post-order Traversal:", post_order(0))