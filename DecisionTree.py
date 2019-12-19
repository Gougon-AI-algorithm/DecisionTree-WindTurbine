import math
import Constant
import Node


class DecisionTree:
    def __init__(self, dataframe):
        self.dataframe = dataframe

        self.all_labels = self._get_labels()
        self.p_conditions = Constant.P_NODES_INTERVAL

        self.root = self._make_decision_tree(self.dataframe, self.all_labels, '', 0)
        self.print_tree(self.root)

    def predict(self, params):
        node = self.root
        while not len(node.get_children()) == 0:
            predict_attr = node.get_value()
            print('predict attr = ', predict_attr)
            predict_order = Constant.ATTRS_NAME.index(predict_attr)
            for condition_num in range(len(self.all_labels[predict_attr]) - 1):
                left_margin = self.all_labels[predict_attr][condition_num]
                right_margin = self.all_labels[predict_attr][condition_num + 1]
                if left_margin <= params[predict_order] < right_margin:
                    node = node.get_children()[condition_num]
        print(node.get_cluster())

    def _get_labels(self):
        nodes = {}
        attrs = [self.dataframe[Constant.WS_ATTR_NAME], self.dataframe[Constant.RM_ATTR_NAME],
                 self.dataframe[Constant.CM_ATTR_NAME], self.dataframe[Constant.RS_ATTR_NAME]]
        attr_order = 0
        for attr in attrs:
            attr_labels = self._get_attr_labels(attr)
            nodes[Constant.ATTRS_NAME[attr_order]] = attr_labels
            attr_order += 1
        return nodes

    def _get_attr_labels(self, attr):
        self._do_nothing()
        min_val = min(attr)
        max_val = max(attr)
        interval = (max_val - min_val) / Constant.CLUSTER_NUMBER
        attr_labels = []
        for interval_num in range(Constant.CLUSTER_NUMBER + 1):
            cut_point = min_val + (interval * interval_num)
            attr_labels.append(cut_point)
        return attr_labels

    def _make_decision_tree(self, data_set, labels, cur_label, depth):
        clone_labels = labels.copy()
        node = Node.Node()
        label = self._get_highest_information_gain_label(data_set, clone_labels)

        if label == cur_label:
            return None

        node.set_value(label)
        children = []

        if depth == len(Constant.ATTRS_NAME) - 2:
            p_conditions = {}
            for data in data_set[Constant.P_ATTR_NAME]:
                self._add_data_into_condition_counts(data, p_conditions)
            node.set_cluster(max(p_conditions, key=p_conditions.get))
            return node

        for condition_num in range(len(self.all_labels[label]) - 1):
            clone_data_set = self._split_data_set(data_set, label, condition_num)
            if len(clone_data_set) == 0:
                break
            node.set_cluster(self.all_labels[label][condition_num])
            children.append(self._make_decision_tree(clone_data_set, clone_labels, label, depth + 1))

        node.set_children(children)
        return node

    def _get_highest_information_gain_label(self, data_set, labels):
        information_gains = {}
        for label in labels:
            clone_data_set = data_set.copy()
            information_gains[label] = self._get_information_gain(clone_data_set, label)
        print(information_gains)
        return min(information_gains, key=information_gains.get)

    def _get_information_gain(self, data_set, label):
        information_gain = 0
        total_data_set_length = len(data_set)
        for condition_num in range(len(self.all_labels[label]) - 1):
            left_margin = self.all_labels[label][condition_num]
            right_margin = self.all_labels[label][condition_num + 1]
            clone_data_set = data_set[data_set[label] >= left_margin]
            clone_data_set = clone_data_set[clone_data_set[label] < right_margin]
            entropy = self._calc_entropy(clone_data_set[Constant.P_ATTR_NAME])
            information_gain += (len(clone_data_set) / total_data_set_length) * entropy
        return information_gain

    def _calc_entropy(self, data_set):
        condition_counts = {}
        for data in data_set:
            self._add_data_into_condition_counts(data, condition_counts)
        entropy = 0
        for condition_count in condition_counts.values():
            prob = condition_count / len(data_set)
            entropy -= prob * math.log2(prob)
        return entropy

    def _add_data_into_condition_counts(self, data, condition_counts):
        self._do_nothing()
        for p_condition_num in range(len(self.p_conditions) - 1):
            left_margin = self.p_conditions[p_condition_num]
            right_margin = self.p_conditions[p_condition_num + 1]
            if left_margin <= data < right_margin:
                if left_margin not in condition_counts.keys():
                    condition_counts.setdefault(left_margin, 0)
                condition_counts[left_margin] += 1

    def _split_data_set(self, data_set, label, condition_count):
        left_margin = self.all_labels[label][condition_count]
        right_margin = self.all_labels[label][condition_count + 1]
        clone_data_set = data_set[left_margin <= data_set[label]]
        clone_data_set = clone_data_set[clone_data_set[label] < right_margin]
        return clone_data_set

    def get_labels(self):
        return self.all_labels

    def print_tree(self, node):
        if node is None:
            return
        print(node.get_value(), end=' ')
        print(node.get_cluster(), end='')
        if not len(node.get_children()) == 0:
            print('[', end='')
        for children in node.get_children():
            self.print_tree(children)
            if not node.get_children()[-1] == children:
                print(',', end='')
        if not len(node.get_children()) == 0:
            print(']', end='')

    def _do_nothing(self):
        pass
