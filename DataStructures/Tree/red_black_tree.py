import rbt_node as rbt
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

def default_compare(a, b):
    
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

def rotate_left(my_node):
    
    x = my_node["right"]
    my_node["right"] = x["left"]
    x["left"] = my_node
    rbt.change_color(x, my_node["color"])
    rbt.change_color(my_node, rbt.RED)
    x["size"] = my_node["size"]
    my_node["size"] = 1 + size(my_node["left"]) + size(my_node["right"])
    return x

def rotate_right(my_node):
    
    x = my_node["left"]
    my_node["left"] = x["right"]
    x["right"] = my_node
    rbt.change_color(x, my_node["color"])
    rbt.change_color(my_node, rbt.RED)
    x["size"] = my_node["size"]
    my_node["size"] = 1 + size(my_node["left"]) + size(my_node["right"])
    return x

def flip_colors(my_node):
    
    rbt.change_color(my_node, rbt.RED)
    rbt.change_color(my_node["left"], rbt.BLACK)
    rbt.change_color(my_node["right"], rbt.BLACK)
    
def flip_node_color(my_node):
    
    if my_node is not None:
        if rbt.is_red(my_node):
            rbt.change_color(my_node, rbt.BLACK)
        else:
            rbt.change_color(my_node, rbt.RED)
            
def size_tree(root):
    
    if root is None:
        return 0
    else:
        return root["size"]

def get_node(root, key):
    
    if root is None:
        return None
    cmp = default_compare(key, rbt.get_key(root))
    if cmp < 0:
        return get_node(root["left"], key)
    elif cmp > 0:
        return get_node(root["right"], key)
    else:
        return root

def get(my_node, key):
    return get_node(my_node, key)
    
def contains(my_node, key):
    return get_node(my_node, key) is not None

def size(my_node):
    
    if my_node is None:
        return 0
    else:
        return my_node["size"]

def is_empty(my_node):
    return size(my_node) == 0

def key_set_tree(root, key_set):
    
    if root is None:
        return key_set
    al.add_last(key_set, rbt.get_key(root))
    key_set_tree(root["left"], key_set)
    key_set_tree(root["right"], key_set)
    return key_set

def key_set(my_node):
    key_set = al.new_list()
    return key_set_tree(my_node, key_set)

def value_set_tree(root, value_set):
    
    if root is None:
        return value_set
    al.add_last(value_set, rbt.get_value(root))
    value_set_tree(root["left"], value_set)
    value_set_tree(root["right"], value_set)
    return value_set

def value_set(my_node):
    value_set = al.new_list()
    return value_set_tree(my_node, value_set)

def get_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return rbt.get_key(root)
    else:
        return get_min_node(root["left"])

def get_min(my_rbt):
    return get_min_node(my_rbt["root"])

def get_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return rbt.get_key(root)
    else:
        return get_max_node(root["right"])

def get_max(my_rbt):
    return get_max_node(my_rbt["root"])

def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list

    key = rbt.get_key(root)

    if key_initial < key:
        values_range(root["left"], key_initial, key_final, value_list)

    if key_initial <= key <= key_final:
        sl.add_last(value_list, rbt.get_value(root))

    if key < key_final:
        values_range(root["right"], key_initial, key_final, value_list)

    return value_list

def values(my_rbt, key_initial, key_final):
    value_list = sl.new_list()
    values_range(my_rbt["root"], key_initial, key_final, value_list)
    return value_list