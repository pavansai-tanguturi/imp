class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, root, key):
        # Standard BST insertion
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed
        
        # Update height of current node
        self.update_height(root)
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, key):
        if not root:
            return root
        
        # Standard BST delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        # Update height
        self.update_height(root)
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        
        # Left Right Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        
        # Right Left Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

# Function to get user input and perform operations
def main():
    avl = AVLTree()
    while True:
        print("\nAVL Tree Operations:")
        print("1. Insert a key")
        print("2. Delete a key")
        print("3. Print inorder traversal")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                key = int(input("Enter key to insert: "))
                avl.root = avl.insert(avl.root, key)
                print(f"Inserted {key}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == '2':
            try:
                key = int(input("Enter key to delete: "))
                avl.root = avl.delete(avl.root, key)
                print(f"Deleted {key} (if it existed)")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == '3':
            result = avl.inorder(avl.root)
            if result:
                print("Inorder traversal:", result)
            else:
                print("Tree is empty")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()