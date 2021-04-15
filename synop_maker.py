import info_finder
import pdb

class SynopMaker:
    def __init__(self):
        pass

    def get_synop(self, movie_name):
        info = info_finder.InfoFind(movie_name + " movie") 
        return info.GetInfo()
        
    def make_file(self):
        return open("synopsis", "w")

    def write_synop(self, movie_name):
        text = self.make_file()
        synopsis = self.get_synop(movie_name)
        text.write(synopsis)
        text.close()


#poop = SynopMaker()
#poop.write_synop()
#poop.write_synop("10 things I hate about you")





    


