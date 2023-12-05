
import pandas as pd

def load_and_concat_list_of_txt(list_dot_txt_by_state:list,)->pd.DataFrame:
    pd_list=[]

    for my_file in list_dot_txt_by_state:

        #
        pd_list.append(
            pd.read_csv(
                filepath_or_buffer=my_file,
                header=None,
                skiprows=[0],
                names=["state","sex","year","name","count"]
            )
        )
    return pd.concat(pd_list,axis=0)