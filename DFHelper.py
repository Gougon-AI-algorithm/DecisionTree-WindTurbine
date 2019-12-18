class DFHelper:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_dataframe(self):
        return self.dataframe

    def choose_necessary_data(self, attrs):
        self._clear_unnecessary_attr(attrs)

    def _clear_unnecessary_attr(self, attrs):
        self.dataframe = self.dataframe[attrs]

    def drop_na(self):
        self.dataframe = self.dataframe.dropna()

    def values(self):
        return self.dataframe.values

    def head(self):
        print(self.dataframe.head())

    def get_column(self, name):
        return self.dataframe[name]

