class Node:
    def __init__(self):
        self.value = 0
        self.children = []
        self.entropy = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_children(self):
        return self.children

    def set_children(self, children):
        if isinstance(children, list):
            self.children = children

    def get_entropy(self):
        return self.entropy

    def set_entropy(self, entropy):
        self.entropy = entropy
