import pandas as pd
import Constant


class DFHelper:
    def __init__(self):
        self.dataframe = pd.DataFrame()

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def get_dataframe(self):
        return self.dataframe

    def choose_necessary_data(self, attrs):
        self._clear_unnecessary_attr(attrs)

    def _clear_unnecessary_attr(self, attrs):
        self.dataframe = self.dataframe[attrs]

    def drop_na(self):
        self.dataframe.dropna()

    def transform_df_to_float(self):
        attr_names = [Constant.WS_ATTR_NAME, Constant.RM_ATTR_NAME,
                      Constant.CM_ATTR_NAME, Constant.RS_ATTR_NAME, Constant.P_ATTR_NAME]
        for attr_name in attr_names:
            self.dataframe[attr_name] = self.dataframe[attr_name].astype(float)

    def head(self):
        print(self.dataframe.head())

    def get_column(self, name):
        return self.dataframe[name]

