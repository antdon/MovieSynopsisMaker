import info_finder
import pdb

class SynopMaker:
    """
    Class containing functions related to writing synopsis to a file
    """
    def __init__(self):
        pass

    def get_synop(self, movie_name):
        """
        Gets the synopsis for movie_name
        Parameters:
            movie_name - title of the movie
        Return:
            - String synopsis
        """
        info = info_finder.InfoFind(movie_name + " movie") 
        return info.GetInfo()
        
    def make_file(self):
        """
        Creates a new file called synopsis 
        If such a file exist this function wipes it
        Return:
            - file object of synopsis file
        """
        return open("synopsis", "w")

    def write_synop(self, movie_name):
        """
        writes the a synopsis into a file
        Parameters:
            movie_name - name of movie  to be synopsised
        """
        text = self.make_file()
        synopsis = self.get_synop(movie_name)
        text.write(synopsis)
        text.close()







    


