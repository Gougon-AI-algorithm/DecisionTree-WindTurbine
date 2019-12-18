import math
import Constant
import DFHelper


class DecisionTree:
    def __init__(self, df_helper):
        self.df_helper = df_helper
        self._raise_df_helper_type()

        self.df_helper.choose_necessary_data(Constant.ATTRS_NAME)
        self.df_helper.drop_na()

        self.attrs = [df_helper.get_column(Constant.WS_ATTR_NAME), df_helper.get_column(Constant.RM_ATTR_NAME),
                      df_helper.get_column(Constant.CM_ATTR_NAME), df_helper.get_column(Constant.RS_ATTR_NAME)]
        self.attrs_labels = self._get_attrs_labels()
        self.p = df_helper.get_column(Constant.P_ATTR_NAME)
        self.p_labels = Constant.P_NODES_INTERVAL
        self._make_decision_tree()

    def _raise_df_helper_type(self):
        if not isinstance(self.df_helper, DFHelper.DFHelper):
            raise TypeError(Constant.DF_HELPER_TYPE_ERROR)

    def _get_attrs_labels(self):
        nodes = {}
        for attr_order in range(len(self.attrs)):
            attr_labels = self._get_attr_labels(attr_order)
            nodes[Constant.ATTRS_NAME[attr_order]] = attr_labels
        return nodes

    def _get_attr_labels(self, attr_order):
        attr = self.attrs[attr_order]
        min_val = min(attr)
        max_val = max(attr)
        interval = (max_val - min_val) / Constant.CLUSTER_NUMBER
        attr_labels = []
        for interval_num in range(Constant.CLUSTER_NUMBER + 1):
            cut_point = min_val + (interval * interval_num)
            attr_labels.append(cut_point)
        return attr_labels

    def _make_decision_tree(self):
        entropy = self._calc_entropy(self.p, self.p_labels)
        information_gain = 0

    def _calc_entropy(self, data_set, labels):
        label_counts = {}
        for data in data_set:
            self._add_data_into_label_counts(data, label_counts, labels)
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

    def get_attrs_labels(self):
        return self.attrs_labels

    def _do_nothing(self):
        pass

