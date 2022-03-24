# ME640 Assignment 5: Graphing and Planning

This code is developed for Section 4 of Assignment 5 for ME640 Winter 2022.

This code creates a random number of nodes *N* and edges based on the specified input and then uses the A* algorithm to calculate the shortest path from node 1 to N.

## Getting Started

### Dependencies

* Python 3
* Matplotlib 3.5 or higher
```
pip install matplotlib==3.5
```

### Executing program

* Run main.py and specify *-n/--nodes* for the number of nodes and *-e/--edges* for the number of edges

Sample run:

To generate 100 nodes and 60 edges

```
python3 main.py -n 100 -e 60
```

* If no shortest path is found, the code will plot the graph and display an error message indicating that no path was found.