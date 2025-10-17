from DataStructures.Tree import bst_node as n


def new_map():
    """Create a new empty BST container.

    The map is represented as a dict with a single key "root" whose value
    is either None or a bst_node created by `bst_node.new_node`.
    """
    return {"root": None}


def _node_size(node):
    return node["size"] if node is not None else 0


def _insert(node, key, value):
    """Recursive helper that inserts key/value into subtree rooted at node.

    Returns the (possibly new) root node of the subtree.
    """
    if node is None:
        return n.new_node(key, value)

    if key < node["key"]:
        node["left"] = _insert(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = _insert(node["right"], key, value)
    else:
        # update existing key
        node["value"] = value

    # update size
    node["size"] = 1 + _node_size(node["left"]) + _node_size(node["right"])
    return node


def put(bst, key, value):
    """Insert or update (key, value) into the BST container `bst`.

    Returns the bst dict (same object) to match tests' expectations.
    """
    bst["root"] = _insert(bst.get("root"), key, value)
    return bst


def get(bst, key):
    """Return the value associated with key in bst or None if not found."""
    node = bst.get("root")
    while node is not None:
        if key == node["key"]:
            return node["value"]
        elif key < node["key"]:
            node = node["left"]
        else:
            node = node["right"]
    return None


def size_tree(node):
    return _node_size(node)


def size(bst):
    if bst is None:
        return 0
    return size_tree(bst.get("root"))

def contains(bst, key):
    return get(bst, key) != None

def is_empty(bst):
    return size(bst) == 0

def key_set_tree(root, key_list):
    if root is None:
        return
    key_set_tree(root["left"], key_list)
    key_list.append(root["key"])
    key_set_tree(root["right"], key_list)
    
def key_set(bst):
    key_list = []
    key_set_tree(bst.get("root"), key_list)
    return key_list

def value_set_tree(root, value_list):
    if root is None:
        return
    value_set_tree(root["left"], value_list)
    value_list.append(root["value"])
    value_set_tree(root["right"], value_list)
    
def value_set(bst):
    value_list = []
    value_set_tree(bst.get("root"), value_list)
    return value_list

def get_min_node(root):
    if root is None:
        return None
    while root["left"] is not None:
        root = root["left"]
    return root

def get_min(bst):
    min_node = get_min_node(bst.get("root"))
    if min_node is None:
        return None
    return (min_node["key"], min_node["value"])

def get_max_node(root):
    if root is None:
        return None
    while root["right"] is not None:
        root = root["right"]
    return root

def get_max(bst):
    max_node = get_max_node(bst.get("root"))
    if max_node is None:
        return None
    return (max_node["key"], max_node["value"])

def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root

def delete_min(bst):
    bst["root"] = delete_min_tree(bst.get("root"))
    return bst

def delete_max_tree(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root

def delete_max(bst):
    bst["root"] = delete_max_tree(bst.get("root"))
    return bst

def height_tree(root):
    if root is None:
        return -1
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def height(bst):
    return height_tree(bst.get("root"))

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        list_key.append(root["key"])
    if key_final > root["key"]:
        keys_range(root["right"], key_initial, key_final, list_key)

def keys(bst, key_initial, key_final):
    list_key = []
    keys_range(bst.get("root"), key_initial, key_final, list_key)
    return list_key

def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, list_value)
    if key_initial <= root["key"] <= key_final:
        list_value.append(root["value"])
    if key_final > root["key"]:
        values_range(root["right"], key_initial, key_final, list_value)
        
def values(bst, key_initial, key_final):
    list_value = []
    values_range(bst.get("root"), key_initial, key_final, list_value)
    return list_value