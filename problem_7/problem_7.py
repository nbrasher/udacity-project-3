'''
Problem 7: HTTPRouter using a Trie
'''

# Basic Trie node plus handler 
class RouteTrieNode:
    def __init__(self, handler: str = None):
        self.children = {}
        self.handler = handler

    def insert(self, path: str, handler: str=None):
        self.children[path] = RouteTrieNode(handler)

# Trie structure to store routes and associated handlers
class RouteTrie:
    def __init__(self,
                 root_handler: str,
                 not_found_handler: str):
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, 
               path: str, 
               handler: str = None):
        ''' Inserts path one chunk at a time into the Trie
        '''
        # Start at the root node
        node = self.root

        # Iterate along supplied path
        for p in path.split('/'):
            # Filter out empty blocks
            if p:
                node.insert(p, self.not_found_handler)
                node = node.children[p]
        
        node.handler = handler


    def find(self, path: str):
        ''' Traverse Route Trie, returning not_found_handler if path 
                does not exist
        '''
        node = self.root

        # Traverse Trie
        for p in path.split('/'):
            if p:
                if p in node.children.keys():
                    node = node.children[p]
                else:
                    return self.not_found_handler
        
        # Return handler if traversed to the end
        return node.handler


# Wrapper class to handle input
class Router:
    def __init__(self,
                 root_handler: str,
                 not_found_handler: str):
        self.trie = RouteTrie(root_handler, 
                              not_found_handler)

    def add_handler(self, path: str, handler: str):
        self.trie.insert(path, handler)

    def lookup(self, path: str):
        return self.trie.find(path)


if __name__ == '__main__':
    # Create the router and add a route
    router = Router(root_handler="root handler", 
                    not_found_handler="not found handler")
    router.add_handler(path="/home/about", 
                       handler="about handler")

    print(router.lookup("/")) # Should print 'root handler'
    print(router.lookup("/home")) # Should print 'not found handler'
    print(router.lookup("/home/about")) # Should print 'about handler'
    print(router.lookup("/home/about/")) # Should print 'about handler'
    print(router.lookup("/home/about/me")) # Should print 'not found handler'   