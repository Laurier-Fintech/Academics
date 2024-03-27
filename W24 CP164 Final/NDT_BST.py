"""
-------------------------------------------------------
NDT_BST
-------------------------------------------------------
Author:
ID:
Email:
__updated__ = ""
-------------------------------------------------------

Name:           The Binary Tree Class
Created By:     Jason Van Humbeck
Package:        Laurier FinTech CP164 Mock Exam - Part 2

Task Description:
    This is a Basic Binary Search Tree. It is your job to complete all of the empty
    methods, and ensure they work in all circumstances. The class design is up to you...
    however, you are encourage to use auxiliary functions where necessary.

Requirements:
    - No Imported Classes Allowed
    - Prohibit the use of loop breaks.
    - No illegal aids.
"""
class BST:
    def insert(self, data):
        """
        -------------------------------------------------------
        Inserts a node into the BST. There are no duplicates.
        Use: status = self.insert(data)
        -------------------------------------------------------
        Parameters:
            data - a comparable data element (?)
        Returns:
            status - 1 if the value is inserted into the BST,
                     0 otherwise.
        -------------------------------------------------------
        """
        if not self.exists(self._root, data):
            self._root = self.aux_insert(self._root, data)
            return 1
        else:
            return 0


    def aux_insert(self, root, data):
        """
        *AUXILIARY FUNCTION*
        -------------------------------------------------------
        Inserts a node into the BST. There are no duplicates.
        Private helper function.
        Use: node = self._insert(node, data)
        -------------------------------------------------------
        Parameters:
            root - a BST node (_BSTNode)
            data - a comparable data element (?)
        Returns:
            node - the current node (_BSTNode)
        -------------------------------------------------------
        """
        if not root:
            return TNODE(data, None, None)
        if data < root._data:
            root._left = self.aux_insert(root._left, data)
        elif data > root._data:
            root._right = self.aux_insert(root._right, data)
        return root

    def exists(self, node, data):
        """
        -------------------------------------------------------
        Determines if a value exists in the BST stemming from node.
        Use: exists = self.exists(node, data)
        -------------------------------------------------------
        Parameters:
            node - a BST node (_BSTNode)
            data - a comparable data element (?)
        Returns:
            exists - True if data is found in the BST, False otherwise.
        -------------------------------------------------------
        """
        if not node:
            return False
        if node._data == data:
            return True
        else:
            return self.exists(node._left, data) or self.exists(node._right, data)


    def siblings(self, n1, n2):
        """
        -------------------------------------------------------
        Determines if the nodes which contain values n1 and n2
        are adjacent. This is proven if they have the same parent.
        Use: adjacents = self.aux_siblings(parent, n1, n2)
        -------------------------------------------------------
        Parameters:
            n1 - a node value (*)
            n2 - a node value (*)
        Returns
            adjacents - True if it is determined that the nodes
            are adjacent; False if otherwise.
        -------------------------------------------------------
        """
        return self.aux_siblings(self._root, n1, n2)

    def aux_siblings(self, parent, n1, n2):
        """
        *AUXILIARY FUNCTION*
        -------------------------------------------------------
        Determines if the nodes which contain values n1 and n2
        are adjacent. This is proven if they have the same parent.
        Use: adjacents = self._are_adjacents_aux(parent, v1, v2)
        -------------------------------------------------------
        Parameters:
            parent - a BST node (_BSTNode)
            n1 - a node value (*)
            n2 - a node value (*)
        Returns
            adjacents - True if it is determined that the nodes
            are adjacent; False if otherwise.
        -------------------------------------------------------
        """
        if parent is None:
            return False

        if parent._left is not None and parent._right is not None:
            if (parent._left._data == n1 and parent._right._data == n2) or (parent._left._data == n2 and parent._right._data == n1):
                return True
            else:
                return self.aux_siblings(parent._left, n1, n2) or self.aux_siblings(parent._right, n1, n2)
        elif parent._right is not None:
            return self.aux_siblings(parent._right, n1, n2)
        elif parent._left is not None:
            return self.aux_siblings(parent._left, n1, n2)
        else:
            return False


    def total_nodes(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = self.total_nodes()
        -------------------------------------------------------
        Returns:
            n - number of nodes in the BST (int)
        -------------------------------------------------------
        """
        return self.aux_total_nodes(self._root)

    def aux_total_nodes(self, root):
        """
        *AUXILIARY FUNCTION*
       -------------------------------------------------------
       Returns the number of nodes in the BST.
       Private helper function.
       Use: n = self._total_nodes(node)
       -------------------------------------------------------
       Parameters:
           root - a BST node (_BSTNode)
       Returns:
           n - number of nodes in the BST (int)
       -------------------------------------------------------
       """
        if not root:
            return 0
        else:
            return 1 + self.aux_total_nodes(root._right) + self.aux_total_nodes(root._left);

    def find_vein(self, data):
        """
        -------------------------------------------------------
        Finds the path from the root to a node containing data.
        Use: path = self.find_vein(data)
        -------------------------------------------------------
        Parameters:
            data - a comparable data element (?)
        Returns:
            path - a list of data values from the root to a node
                   containing data, None if data is not in the BST (list)
        -------------------------------------------------------
        """
        if self.exists(self._root, data):
            return self.aux_find_vein(self._root,data)
        return []

    def aux_find_vein(self, root, data):
        """
        *AUXILIARY FUNCTION*
        -------------------------------------------------------
        Finds the path from the root to a node containing data.
        Private helper function.
        Use: path = self._find_vein(node, data)
        -------------------------------------------------------
        Parameters:
            root - a BST node (_BSTNode)
            data - a comparable data element (?)
        Returns:
            path - a list of data values from the root to a node
                   containing data, None if data is not in the BST (list)
        -------------------------------------------------------
        """
        if not root:
            return []
        if root._data == data:
            return [data]
        if root._data < data:
            return [root._data] + self.aux_find_vein(root._right, data)
        else:
            return [root._data] + self.aux_find_vein(root._left, data)

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================
    def __init__(self):
        """
       -------------------------------------------------------
       Initializes an empty BST.
       Use: bst = BST()
       -------------------------------------------------------
       Returns:
           A new BST object (BST)
       -------------------------------------------------------
       """
        self._root = None

    def test(self, root):
        """
        -------------------------------------------------------
        Traverses the BST in pre-order (root, left, right) manner
        and returns a string used for internal comparison.
        Use: traversal = self.test(root)
        -------------------------------------------------------
        Parameters:
            root - a BST node (_BSTNode)
        Returns:
            traversal - a string representing the pre-order traversal
                        of the BST (str)
        -------------------------------------------------------
        """
        if not root:
            return ""
        out = ""
        out += f'{root._data}'
        out += self.test(root._left)
        out += self.test(root._right)
        return out

    def print_bst(self, tabs):
        """
        -------------------------------------------------------
        Prints the BST in a readable format.
        Use: self.print_bst(tabs)
        -------------------------------------------------------
        Parameters:
            tabs - the number of tabs to start with (int)
        Returns:
            None
        -------------------------------------------------------
        """
        self.aux_print_bst(self._root, tabs)

    def aux_print_bst(self, node, tabs):
        """
        *AUXILIARY FUNCTION*
        -------------------------------------------------------
        Prints the BST rooted at the given node in a readable format.
        Private helper function for print_bst.
        -------------------------------------------------------
        Parameters:
            node - the root of the subtree to print (TNODE)
            tabs - the number of tabs to start with (int)
        Returns:
            None
        -------------------------------------------------------
        """
        if not node:
            return
        store = ""
        for i in range(tabs):
            if tabs - i == 1:
                store += "|___"
            else:
                store += "\t"

        print(f'{store}| -> {node._data}')
        self.aux_print_bst(node._left, tabs + 1)
        self.aux_print_bst(node._right, tabs + 1)


class TNODE:
    def __init__(self, data, left_node, right_node):
        """
        -------------------------------------------------------
        Initializes a node for use in a binary search tree.
        Use: node = TNODE(data, lNode, rNode)
        -------------------------------------------------------
        Parameters:
            data - a comparable data element (?)
            lNode - the left child node (TNODE)
            rNode - the right child node (TNODE)
        Returns:
            A new TNODE object (TNODE)
        -------------------------------------------------------
        """
        self._data = data
        self._left = left_node
        self._right = right_node
