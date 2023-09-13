class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        if self.root is None:
            return None
        
        # Helper function for depth-first traversal
        def dfs_search(node):
            if node.get('id') == target_id:
                return node

            for child in node.get('children', []):
                result = dfs_search(child)
                if result:
                    return result

            return None

        return dfs_search(self.root)
