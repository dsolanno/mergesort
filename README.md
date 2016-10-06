README.md

# Merge Sort algorithm
Python implementation.
Testing solutions for alphabetically sorting a file whose content does not fit in memory.


### Pseucode 

Given a file that potenttially could not fit in memory:
* Get available memory in the system (with an offset)
* Second step. Open input file
* Third step, read first line and calculate size in memory
* Chunk lines into groups of M
* Loop. Until chunk size is fitted:
	*   Sort M
	*  Create new File f
	*  Dump sorted(M) to file f
	* Close file f
	
* Create output file F
* Create list L of size N (where N is the number of files created)
* For each generated file:
    * Read a line l from each file f
    * Add (l,f) to L
    * Repeat while L is not empty:
        * Sort L:
            * write l from first element to F
            * read next line l2 from f from first element
            * delete first element
            * add (l2,f) to L


## To be decided:
* List sorting strategy
    * Custom Quick sort
    * Python sorting function
    * UNIX file sorting
    * Others
    
* Strategy to decide chunks size
    * By memory size
        * Each file of size total_memory/n
            * Potential problems: 
                * Setting an small size could result into a large number of files, making impossible to read a line from each one with the current memory 
                * Using n=1 can give problems since memory is a resource that can be accessed by other processes
    * By num lines
        * Potential problem: if lines are too big and memory is small, is possible to overfit it.  
    


## References:
[![N|Solid](https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/220px-Wikipedia-logo-v2.svg.png)](https://nodesource.com/products/nsolid)

Algorithms explanation:

  - Merge Sort (https://en.wikipedia.org/wiki/Merge_sort)
  - Quick Sort (https://en.wikipedia.org/wiki/Quicksort)
  - External sorting (https://en.wikipedia.org/wiki/External_sorting)

You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop files into Dillinger
  - Export documents as Markdown, HTML and PDF


License
----

MIT


**Free Software, Hell Yeah!**


Created by David Solans