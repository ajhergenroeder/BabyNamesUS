import os
import glob
home = os.environ["HOME"]
repo = os.path.join(home,'_git_repos/BabyNamesUS')
package = os.path.join(repo,"src/BabyNamesUS")
datasets = os.path.join(package,'datasets')
raw_namesbystate = os.path.join(datasets,"raw_namesbystate")

filename_dot_txt_by_state_list = glob.glob(
    os.path.join(
        raw_namesbystate,
        "*.TXT"
    )
)
