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