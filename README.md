# Movie Synopsis Maker 
## Synopsis
This script takes a directory filled with movie folders and adds a text file to each directory. This text file contains the first paragraph 
of the wikipedia page for the movie in question; typically a synopsis of the movie.
## How to Use
1. git clone the repository 
```
git clone https://github.com/antdon/MovieSynopsisMaker.git
```
2. cd into the cloned dir
```
cd MovieSynopsisMaker
```
3. edit the PATH vairable in run.py to your movie folder
4. set up virtual env
```
source venv/bin/activate
```
5. Run
```
python3.9 run.py
```
## Movie folder format
The movie folder should consist of seperate directorys for each movie with the title of the movie also being the title of the directory

## Improvements
This project can always be improved by adding selenium edge cases. There are some movies where the xpath of the first paragraph of the wikipedia page 
is different. These cases can be added to the potential_synop_xpath List variable in infofinder.py. If the a movie synopsis' xpath is not in the List
"could not find synopsis for (movie name)" will be printed to stderr and the string "could not find synopsis" will be written into the movies synopsis 
file
