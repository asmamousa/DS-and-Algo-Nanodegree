class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, partial_path):
        self.children[partial_path] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, splitted_path_list, handler):
        current_node = self.root

        for partial_path in splitted_path_list:
            if partial_path not in current_node.children:
                current_node.insert(partial_path)
            current_node = current_node.children[partial_path]

        current_node.handler = handler

    def find(self, splitted_path_list):
        current_node = self.root

        for partial_path in splitted_path_list:
            if partial_path not in current_node.children:
                return None
            current_node = current_node.children[partial_path]

        return current_node.handler


class Router:
    def __init__(self, handler):
        self.route_trie = RouteTrie()
        self.route_trie.handler = handler

    def add_handler(self, full_path, handler):
        if len(handler) == 0 or handler == None:
            raise Exception("Handler can't be Null")

        splitted_path_list = self.split_path(full_path)
        self.route_trie.insert(splitted_path_list, handler)

    def lookup(self, full_path):
        if full_path == None or len(full_path):
            raise Exception("Path can't be Null")
        splitted_path_list = self.split_path(full_path)
        if splitted_path_list == '/':
            return self.route_trie.handler
        return self.route_trie.find(splitted_path_list)


    def split_path(self, full_path):
        if full_path == '/':
            return full_path
        path_list = full_path.split('/')
        filtered_splitted_list = list(filter(None, path_list))
        return filtered_splitted_list


router = Router("root handler")
router.add_handler("/home/about", "about handler")


print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me"))

print(router.lookup(None))
# raise Exception: Path can't be Null

router.add_handler("/Docs/projects/", '')
# raise Exception: Handler can't be Null
