## CS415 Project 3: Knapsack
### Ari Encarnacion, Vincent Valenzuela

### Setup
To obtain this repository, run the following command:
```
$ git clone <repoLink>
```
To run this project, please use Python interpreter **3.7+**.
The modules used for this project are:
```
sys
math
matplotlib.pyplot
time
```
Please install these through your preferred method if need be.

#

### Running the Program
In this project we compare the time and space efficiencies of different programming techniques 
for solving the Knapsack problem. 
Our tasks employ **Dynamic Programming** and an approach based on the **Greedy Algorithm**.

The folder `KnapsackTestData` contains files of the form `p<num>_<char>.txt`, where `<num>` is numbers`00` to `08` and 
`<char>` is `c`, `v`, and `w` indicating the capacity, values, and weights respectively. 

To run the program use the commands:

``` 
$ cd CS415_project_03
$ python3 main.py <arg>
```

`<arg>` is an `int` between `0-8` 

This will generate the optimal value and optimal subsets for both the dynamic programming
and greedy-algorithm solutions to the knapsack problem.

#

### Plotting Results
Graphs are output to folder `GenPlots` and have extension `.png`

#### Greedy Algorithm Plots
A scatter plot is used to compare operation time between
two different **Greedy Algorithm** approaches. The traditional
approach uses a merge-sort algorithm with time complexity *O(nlogn)*
while the heap-based approach uses a max-heap and is of time 
complexity *O(n + klogn)*

To generate plots for the **Greedy Approach**

```
$ python3 plot_greedy_time.py
```

#### Dynamic Programming Plots
To find the optimal solution for the space efficient approach to the **dynamic programming** solution,
a scatterplot is generated in order to visualize and compare time-space tradeoffs for differnt
values of `K`. When plotting, optimal values are those that fall as close to the graph's origin as possible.

Small input sizes don't show a consistent pattern. Therefore, the largest file (`p08` from `KnapsackTestData`)
is used. Values of `K` tested are:

`W`, `W/2`, and `2^(n-m) for 1 < m < 6`.

A cluster will be seen in the bottom left hand corner and the labels make it hard to distinguish between
the optimal values. However, that cluster holds our determined optimal value, `k = 2^(n-4)`.

To generate this plot run the following command:
```
$ python3 plot_dp_time_space.py
```
