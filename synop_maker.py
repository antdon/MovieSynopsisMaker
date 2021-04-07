import info_finder

class SynopMaker:
    def __init__(self, movie_name):
        self.movie_name = movie_name

    def get_synop(self):
        info = info_finder.InfoFind(self.movie_name) 
        return info.GetInfo()
        
    def make_file(self):
        return open("synopsis", "w", 1)

    def write_synop(self):
        text = self.make_file()
        synopsis = self.get_synop()
        text.write(synopsis)

poop = SynopMaker("10 things I hate about you movie")
#   poop.write_synop()
poop.write_synop()





    


