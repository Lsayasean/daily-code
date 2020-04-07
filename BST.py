# BST construction

# still a little fuzzy on removal.  will come back later 

# BST basic contains insertion searching and deletion

class BST:
    def _init_(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        # current node is what we call the insertion on, meaning self
        currentNode = self

        # we run this until we break out of it (finds where to put the value)
        while True:
            # if value is less than the  current value, explore left side of tree
            if value < currentNode.value:
                # if we are in end of branch add in the value
                if currentNode.left is None:
                    currentNode.self = BST(value)
                    break
                else:
                    # if we have left sub tree to explore, we move current node to left sub tree
                    currentNode = currentNode.left
            else: 
                # identical for left sub tree
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else: 
                    currentNode = currentNode.right
        # allows us to chain .insert calls, irrelevant 
        return self


    def contains(self, value):
        # start by initializing self to current node
        currentNode = self 

        # while current node is not None, check and compare value
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                # once we find the current value we are done 
                return True
        # returns false if we never find the value
        return False


    # the hardest part of a BST
    def remove(self, value, parentNode = None):
        currentNode = self

        # first find value we are trying to remove then remove it
        while currentNode is not None:
            
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                # we want to keep track on parent node, 
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # case where we find our node and value of current node is = to value of currnt node
                # find the smallest value in sub tree and remove it and replace with parent nde
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    # currentNode.value = smallest value of right sub tree
                    currentNode.right.remove(currentNode.value, currentNode)
                # wwe will come back to root node case
                elif parentNode.left = currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

