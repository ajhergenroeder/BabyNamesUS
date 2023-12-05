class params(object):
    def __init__(self,my_dict):
        super().__init__()

        self.__dict__.update(**my_dict)