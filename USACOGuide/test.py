class Solution:
    def solve(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = Tree(inorder[index])

            root.left = self.solve(preorder, inorder[0:index])
            root.right = self.solve(preorder, inorder[index+1:])
            
            return root
        return None