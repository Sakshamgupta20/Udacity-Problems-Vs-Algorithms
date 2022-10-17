# %%
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self,part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self,parts,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_part = self.root
        for part in parts:
            current_part.insert(part)
            current_part = current_part.children[part]
        current_part.handler = handler

    def find(self,parts):
        current_node = self.root

        for part in parts:
            if part not in current_node.children:
                return None

            current_node = current_node.children[part]
        return current_node.handler

# %%
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, none_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler)
        self.none_handler = none_handler

    def add_handler(self,path,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route.insert(self.split_path(path),handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.route.find(self.split_path(path))
        if handler is None:
            return self.none_handler
        return handler


    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [part for part in path.split("/") if part != '']

# %%


router = Router("Udacity Home Page", "not found handler")
router.add_handler("/udacity", "udacity modules handler")
router.add_handler("/udacity/courses/course", "courses handler")

#Case 1 
print("\nTest Case 1: Check for root handler")
print(router.lookup("/")) # should print 'Udacity Home Page'

#Case 2
print("\nTest Case 2: Check for udacity handler")
print(router.lookup("/udacity")) # should print 'udacity modules handler'
print(router.lookup("/udacity/")) # should print 'udacity modules handler'

#Case 3
print("\nTest Case 3: Check for /udacity/courses")
print(router.lookup("/udacity/courses")) # should print 'not found handler'

#Case 4
print("\nTest Case 4: Check for /udacity/courses/course")
print(router.lookup("/udacity/courses/course")) # should print 'courses handler'

#Case 5
print("\nTest Case 5: Check for udacity/courses/course/12 which doesnt exists")
print(router.lookup("/udacity/courses/course/12")) # should print 'not found handler'

# %%



