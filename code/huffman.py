from abc import abstractmethod


class Node:
    def __init__(self, weight, left_node=None, right_node=None):
        self.weight = weight
        self.left_node = left_node
        self.right_node = right_node

class LeafNode(Node):
    def __init__(self, weight, value, binary_code=None):
        super().__init__(weight)
        self.value = value
        self.binary_code = binary_code

@abstractmethod
def get_char_freq():
    """
    This function will read from a text file and return a dictionary with values and their correlated frequency.
    Example: For string 'abbccc', this function would return {'a':1, 'b':2, 'c':3}
    """
    pass

@abstractmethod
def create_leaf_nodes():
    """
    Take a dictionary of values and return a list of leaf nodes
    """
    pass

@abstractmethod
def optimize_tree():
    """
    Takes a list of single node trees, and creates an optimized tree
    """
    pass

@abstractmethod
def analyze_results():
    """
    Responsible for taking tree and reporting the new size after compression
    """
    pass

def main():


if __name__ == '__main__':
    main()
