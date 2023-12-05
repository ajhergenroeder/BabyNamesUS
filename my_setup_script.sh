conda env create -f setup/environment.yml &&
conda activate BabyNamesUS &&
pip install -e . &&
python -m ipykernel install --user --name BabyNamesUS
