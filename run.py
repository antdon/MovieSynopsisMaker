import os
import synop_maker
from pathlib import Path
import pdb

if __name__ == "__main__":
    PATH = './movies'
    PATH = Path(PATH).resolve()
    for files in os.listdir(path=PATH):
        hemmingway = synop_maker.SynopMaker() 
        files_path = os.path.join(PATH, files)
        os.chdir(files_path)
        hemmingway.write_synop(files)
        os.chdir("..")



