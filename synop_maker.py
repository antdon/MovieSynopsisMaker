import info_finder

class SynopMaker:
    def __init__(self, movie_name):
        self.movie_name = movie_name

    def write_synop(self):
        info = info_finder.InfoFind(self.movie_name) 
        synopsis = info.GetInfo()
        print(synopsis)
        
poop = SynopMaker("10 things I hate about you movie")
poop.write_synop()




    


