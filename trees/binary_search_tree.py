class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # --- RECURSIVE ---

    def insert_recursive(self, val):
        self.root = self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        if node is None:
            return Node(val)
        
        if val < node.val:
            node.left = self._insert_helper(node.left, val)
        elif val > node.val:
            node.right = self._insert_helper(node.right, val)
        return node

    def search_recursive(self, val):
        return self._search_helper(self.root, val)

    def _search_helper(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)

    # --- ITERATIVE ---

    def insert_iterative(self, val):
        if self.is_empty():
            self.root = Node(val)
            return
        
        parent = None
        current = self.root

        while current:
            parent = current
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return
            
        if val < parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)


    def search_iterative(self, val):
        current = self.root
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return True
        return False

    # --- INORDER ---

    def in_order_traversal(self):
        self._in_order_helper(self.root)
        print("None")

    def _in_order_helper(self, node):
        if node is None:
            return
        self._in_order_helper(node.left)
        print(f"{node.val} -> ", end="")
        self._in_order_helper(node.right)

    def in_order_iterative(self):
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(f"{current.val} -> ", end="")
            current = current.right
        print("None")
                

    # --- PREORDER ---
    def pre_order_traversal(self, node):
        if node is None:
            return
        
        print(f"{node.val} -> ")
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
    
    def pre_order_iterative(self):
        if not self.root:
            return
        
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(f"{node.val} -> ", end="")
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print("None")

    # --- POSTORDER ---
    def post_order_traversal(self, node):
        if node is None:
            return
        
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(f"{node.val} -> ", end="")

    def post_order_iterative(self):
        if self.is_empty():
            return

        stack_one = [self.root]
        stack_two = []

        while stack_one:
            node = stack_one.pop()
            stack_two.append(node)

            if node.left:
                stack_one.append(node.left)
            if node.right:
                stack_one.append(node.right)

        while stack_two:
            node = stack_two.pop()
            print(f"{node.val} -> ", end="")
        print("None")


    # --- DELETE ---

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        if node is None: return None

        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._get_inorder_successor(node.right)

            node.val = successor.val
            
            node.right = self._delete_helper(node.right, successor.val)

        return node 
    
    def _get_inorder_successor(self, node):
        current = node
        while current.left:
            current = current.left
        return current
