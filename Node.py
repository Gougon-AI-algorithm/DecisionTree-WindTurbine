class Node:
    def __init__(self):
        self.value = 0
        self.children = []
        self.cluster = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_children(self):
        return self.children

    def set_children(self, children):
        if isinstance(children, list):
            self.children = children

    def get_cluster(self):
        return self.cluster

    def set_cluster(self, cluster):
        self.cluster = cluster
