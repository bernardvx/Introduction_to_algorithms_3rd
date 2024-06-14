
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def add_child(self, data):

        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)
        
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
        

    def in_order_traversal(self):
        tree_list = []

        if self.left:
            tree_list += self.left.in_order_traversal()

        tree_list.append(self.data)

        if self.right:
            tree_list += self.right.in_order_traversal()
        
        return tree_list
    
    def pre_order_traversal(self):
        tree_list = []

        tree_list.append(self.data)

        if self.left:
            tree_list += self.left.pre_order_traversal()
        
        if self.right:
            tree_list += self.right.pre_order_traversal()
        
        return tree_list
    
    def post_order_traversal(self):
        tree_list = []

        if self.left:
            tree_list += self.left.post_order_traversal()
        
        if self.right:
            tree_list += self.right.post_order_traversal()
        
        tree_list.append(self.data)

        return tree_list

    


def build_tree(tree_list):
    root = Node(tree_list[0])
    for i in range(1, len(tree_list)):
        root.add_child(tree_list[i])

    return root


if __name__ == '__main__':
    numbers = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    numbers_tree = build_tree(numbers)
    print('pre order traversal: ',numbers_tree.pre_order_traversal())
    print('in order traversal: ',numbers_tree.in_order_traversal())
    print('post order traversal: ',numbers_tree.post_order_traversal())
    print(numbers_tree.search(1))
    




