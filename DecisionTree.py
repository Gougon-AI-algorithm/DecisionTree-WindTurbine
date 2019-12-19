import math
import Constant
import Node


class DecisionTree:
    def __init__(self, dataframe):
        self.dataframe = dataframe

        self.all_labels = self._get_labels()
        self.p_conditions = Constant.P_NODES_INTERVAL

        self.root = self._make_decision_tree(self.dataframe, self.all_labels)
        print(self.root)

    def _get_labels(self):
        nodes = {}
        attrs = [self.dataframe.get_column(Constant.WS_ATTR_NAME), self.dataframe.get_column(Constant.RM_ATTR_NAME),
                 self.dataframe.get_column(Constant.CM_ATTR_NAME), self.dataframe.get_column(Constant.RS_ATTR_NAME)]
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

    def _make_decision_tree(self, data_set, labels):
        node = Node.Node()
        label = self._get_highest_information_gain_label(data_set, labels)
        node.set_value(label)
        children = []
        for condition_count in range(len(self.all_labels[label])):
            data_set = self._split_data_set(data_set, label, condition_count)
            children.append(self._make_decision_tree(data_set))
        node.set_children(children)
        return node

    def _get_highest_information_gain_label(self, data_set, labels):
        label_entropy = {}
        for label in labels:
            conditions = labels[label]
            label_entropy[label] = self._calc_entropy(data_set[label], conditions)
        return max(label_entropy, key=label_entropy.get)

    def _split_data_set(self, data_set, label, condition_count):
        left_margin = self.all_labels[label][condition_count]
        right_margin = self.all_labels[label][condition_count + 1]
        data_set = data_set[left_margin <= data_set[label] < right_margin]
        return data_set

    def _calc_entropy(self, data_set, conditions):
        label_counts = {}
        for data in data_set:
            self._add_data_into_label_counts(data, label_counts, conditions)
        entropy = 0
        for label_count in label_counts.values():
            prob = label_count / len(data_set)
            entropy -= prob * math.log2(prob)
        return entropy

    def _add_data_into_label_counts(self, data, label_counts, labels):
        self._do_nothing()
        for label_num in range(len(labels) - 1):
            left_margin = labels[label_num]
            right_margin = labels[label_num + 1]
            if left_margin <= data < right_margin:
                if left_margin not in label_counts.keys():
                    label_counts.setdefault(left_margin, 0)
                label_counts[left_margin] += 1

    def get_labels(self):
        return self.all_labels

    def _do_nothing(self):
        pass

