## CS415 Project 3: Knapsack
### Ari Encarnacion, Vincent Valenzuela

In this project we compare the time and space efficiencies of different programming techniques
in solving the Knapsack problem. 
Our tasks employ **Dynamic Programming** and an approach based on the **Greedy Algorithm**.

The folder `KnapsackTestData` contains files of the form `p<num>_<char>.txt`, where `<num>` is `00-08` and 
`<char>` is `c`, `v`, and `w` indicating the capacity, values, and weights respectively. 

To run the program use the commands:

``` 
$ git clone
$ cd CS415_project_03
$ python3 main.py <arg>
```

`<arg>` is an `int` between `0-8` 

### Plotting Results
Graphs are output to folder `GenPlots` and have extension `.png`


A scatter plot is used to compare operation time between
two different **Greedy Algorithm** approaches. The traditional
approach uses a merge-sort algorithm with time complexity *O(nlogn)*
while the heap-based approach uses a max-heap and is of time 
complexity *O(n + klogn)*

To generate plots for the **Greedy Approach**

```
$ python3 plot_greedy_time.py
```