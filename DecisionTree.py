import Constant
import DFHelper


class DecisionTree:
    def __init__(self, df_helper):
        self.df_helper = df_helper
        self._raise_df_helper_type()

        df_helper.choose_necessary_data(Constant.ATTRS_NAME)
        df_helper.drop_na()

        self.attrs = [df_helper.get_column(Constant.WS_ATTR_NAME), df_helper.get_column(Constant.RM_ATTR_NAME),
                      df_helper.get_column(Constant.CM_ATTR_NAME), df_helper.get_column(Constant.RS_ATTR_NAME)]
        self.nodes = self._get_all_nodes()
        print(self.get_nodes())
        # build decision tree

    def _raise_df_helper_type(self):
        if not isinstance(self.df_helper, DFHelper.DFHelper):
            raise TypeError(Constant.DF_HELPER_TYPE_ERROR)

    def _get_all_nodes(self):
        nodes = {}
        for attr_order in range(len(self.attrs)):
            attr_nodes = self._get_attr_nodes(attr_order)
            nodes[Constant.ATTRS_NAME[attr_order]] = attr_nodes
        return nodes

    def _get_attr_nodes(self, attr_order):
        attr = self.attrs[attr_order]
        min_val = min(attr)
        max_val = max(attr)
        print(Constant.ATTRS_NAME[attr_order], ' min=', min_val, ' max=', max_val)
        interval = (max_val - min_val) / Constant.CLUSTER_NUMBER
        attr_nodes = []
        for interval_num in range(Constant.CLUSTER_NUMBER - 1):
            cut_point = min_val + (interval * (interval_num + 1))
            attr_nodes.append(cut_point)
        return attr_nodes

    def get_nodes(self):
        return self.nodes

