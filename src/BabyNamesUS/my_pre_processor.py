from generic_object import GenericObject
from params import params
from BabyNamesUS.utils_pandas import load_and_concat_list_of_txt

class MyPreprocessor(GenericObject):
    def __init__(self,my_params:params):
        super().__init__(params=params)

    def _load_and_concat_list_of_txt(self,list_dot_txt_by_state:list,)->pd.DataFrame:
        return load_and_concat_list_of_txt(
            list_dot_txt_by_state=list_dot_txt_by_state
        )
