# NHL Team Clustering

Idea is to use data from 2023-2024 seasons statistics and group teams into clustering based on their similarities.
After clustering we can find the teams you might enjoy the most. For example if you like to see goals then teams for you would be
from the cluster which has highest average goals per game.

## Table of contents

- [Data](#Data)
- [Preprocessing](#Preprocessing)
- [Clustering](#Clustering)
- [Selection of K](#Selection of K)
- [K-means with K=4](#K-means with K=4)
- [Finding the most similar team using NearestNeighbor search](#Finding the most similar team using NearestNeighbor search)
- [Finding teams with the highest average goals for and against](#Finding teams with the highest average goals for and against)
- [Conclusion](#Conclusion)

## Data

Data is from [NHL offical website](https://www.nhl.com/stats/teams). Data has statistics on the games played and goals for and against.

**Data**

|    | Team                  |   Season |   GP |   W |   L | T   |   OT |   P |    P% |   RW |   ROW |   S/O Win |   GF |   GA |   GF/GP |   GA/GP |   PP% |   PK% |   Net PP% |   Net PK% |   Shots/GP |   SA/GP |   FOW% |
|---:|:----------------------|---------:|-----:|----:|----:|:----|-----:|----:|------:|-----:|------:|----------:|-----:|-----:|--------:|--------:|------:|------:|----------:|----------:|-----------:|--------:|-------:|
|  0 | Vancouver Canucks     | 20232024 |   35 |  23 |   9 | --  |    3 |  49 | 0.7   |   22 |    23 |         0 |  135 |   88 |    3.86 |    2.51 |  24.2 |  77.8 |      24.2 |      81.5 |       28   |    30   |   50.7 |
|  1 | New York Rangers      | 20232024 |   32 |  23 |   8 | --  |    1 |  47 | 0.734 |   18 |    22 |         1 |  107 |   88 |    3.34 |    2.75 |  31.1 |  85.7 |      27.2 |      87.8 |       30.9 |    29.7 |   54.8 |
|  2 | Vegas Golden Knights  | 20232024 |   35 |  21 |   9 | --  |    5 |  47 | 0.671 |   15 |    17 |         4 |  118 |   95 |    3.37 |    2.71 |  22.5 |  81   |      21.7 |      85.7 |       32.3 |    30.1 |   49.6 |
|  3 | Colorado Avalanche    | 20232024 |   34 |  21 |  11 | --  |    2 |  44 | 0.647 |   20 |    20 |         1 |  124 |  103 |    3.65 |    3.03 |  23.6 |  83.3 |      19.7 |      87.5 |       32.2 |    29.4 |   49.2 |
|  4 | Dallas Stars          | 20232024 |   32 |  20 |   8 | --  |    4 |  44 | 0.688 |   14 |    18 |         2 |  112 |   99 |    3.5  |    3.09 |  22.1 |  86.4 |      19   |      93.2 |       29.8 |    30.7 |   53.5 |
|  5 | Boston Bruins         | 20232024 |   32 |  19 |   7 | --  |    6 |  44 | 0.688 |   15 |    17 |         2 |   98 |   85 |    3.06 |    2.66 |  24.5 |  85.8 |      22.5 |      85.8 |       31   |    32.3 |   50.3 |
|  6 | Winnipeg Jets         | 20232024 |   32 |  20 |   9 | --  |    3 |  43 | 0.672 |   18 |    20 |         0 |  109 |   81 |    3.41 |    2.53 |  18.2 |  75   |      16.2 |      78.1 |       31.1 |    28.8 |   47.3 |
|  7 | Los Angeles Kings     | 20232024 |   30 |  19 |   7 | --  |    4 |  42 | 0.7   |   17 |    18 |         1 |  106 |   71 |    3.53 |    2.37 |  20   |  86.6 |      16.2 |      92.8 |       33.9 |    26.6 |   50.8 |
|  8 | New York Islanders    | 20232024 |   33 |  16 |   8 | --  |    9 |  41 | 0.621 |   12 |    15 |         1 |  103 |  105 |    3.12 |    3.18 |  24.7 |  71   |      23.7 |      79   |       30.1 |    35.7 |   50.7 |
|  9 | Florida Panthers      | 20232024 |   33 |  19 |  12 | --  |    2 |  40 | 0.606 |   17 |    19 |         0 |   96 |   86 |    2.91 |    2.61 |  18.9 |  82.9 |      14.2 |      83.8 |       34.3 |    27.1 |   50.3 |
| 10 | Philadelphia Flyers   | 20232024 |   33 |  18 |  11 | --  |    4 |  40 | 0.606 |   12 |    15 |         3 |   98 |   91 |    2.97 |    2.76 |  10.6 |  85.7 |       8.7 |      92.4 |       32.9 |    28.6 |   46.9 |
| 11 | Toronto Maple Leafs   | 20232024 |   31 |  17 |   8 | --  |    6 |  40 | 0.645 |   10 |    13 |         4 |  111 |  104 |    3.58 |    3.35 |  26.4 |  79.2 |      22   |      83.3 |       32.6 |    32.5 |   53.2 |
| 12 | Tampa Bay Lightning   | 20232024 |   35 |  17 |  13 | --  |    5 |  39 | 0.557 |   14 |    16 |         1 |  117 |  120 |    3.34 |    3.43 |  30.4 |  79.6 |      28.6 |      79.6 |       30.4 |    31.1 |   52   |
| 13 | Washington Capitals   | 20232024 |   31 |  17 |   9 | --  |    5 |  39 | 0.629 |   11 |    14 |         3 |   74 |   83 |    2.39 |    2.68 |  12.4 |  82.7 |      11.2 |      84.7 |       28.1 |    30.7 |   47.3 |
| 14 | Nashville Predators   | 20232024 |   34 |  19 |  15 | --  |    0 |  38 | 0.559 |   14 |    18 |         1 |  106 |  104 |    3.12 |    3.06 |  20.5 |  77.3 |      18   |      80.9 |       29.8 |    31   |   49.2 |
| 15 | Carolina Hurricanes   | 20232024 |   34 |  17 |  13 | --  |    4 |  38 | 0.559 |   13 |    16 |         1 |  110 |  108 |    3.24 |    3.18 |  24.4 |  82.7 |      18.3 |      88.2 |       33.9 |    25.6 |   51.2 |
| 16 | New Jersey Devils     | 20232024 |   32 |  17 |  13 | --  |    2 |  36 | 0.563 |   14 |    17 |         0 |  109 |  114 |    3.41 |    3.56 |  30   |  77.7 |      27   |      79.6 |       31.7 |    29.3 |   53.4 |
| 17 | Arizona Coyotes       | 20232024 |   33 |  17 |  14 | --  |    2 |  36 | 0.545 |   14 |    15 |         2 |  101 |   95 |    3.06 |    2.88 |  23.2 |  80.2 |      18.8 |      82.2 |       27.1 |    31.3 |   47.5 |
| 18 | Detroit Red Wings     | 20232024 |   34 |  16 |  14 | --  |    4 |  36 | 0.529 |   13 |    15 |         1 |  120 |  113 |    3.53 |    3.32 |  21.6 |  79.5 |      18   |      82.8 |       30.1 |    32.2 |   48.8 |
| 19 | St. Louis Blues       | 20232024 |   33 |  17 |  15 | --  |    1 |  35 | 0.53  |   14 |    16 |         1 |   99 |  110 |    3    |    3.33 |  11.6 |  78.9 |       7.4 |      87.8 |       30.7 |    32   |   49.5 |
| 20 | Montréal Canadiens    | 20232024 |   33 |  15 |  13 | --  |    5 |  35 | 0.53  |    7 |    12 |         3 |   92 |  109 |    2.79 |    3.3  |  17.7 |  73   |      12.6 |      75.7 |       29.3 |    33.6 |   53.9 |
| 21 | Pittsburgh Penguins   | 20232024 |   32 |  15 |  13 | --  |    4 |  34 | 0.531 |   12 |    13 |         2 |   91 |   89 |    2.84 |    2.78 |  13.7 |  82.7 |       9.8 |      84.6 |       32.9 |    30.9 |   54.7 |
| 22 | Minnesota Wild        | 20232024 |   32 |  15 |  13 | --  |    4 |  34 | 0.531 |   10 |    12 |         3 |   97 |  101 |    3.03 |    3.16 |  18.2 |  72.2 |      13.6 |      73.9 |       30.2 |    30.3 |   45.3 |
| 23 | Calgary Flames        | 20232024 |   34 |  14 |  15 | --  |    5 |  33 | 0.485 |   11 |    14 |         0 |  102 |  111 |    3    |    3.26 |  11.8 |  83.3 |       8.2 |      91.7 |       31.6 |    29.8 |   50.4 |
| 24 | Seattle Kraken        | 20232024 |   35 |  12 |  14 | --  |    9 |  33 | 0.471 |    9 |    11 |         1 |   94 |  108 |    2.69 |    3.09 |  20.8 |  79.2 |      17   |      81.2 |       29.9 |    29.2 |   48.9 |
| 25 | Buffalo Sabres        | 20232024 |   35 |  14 |  17 | --  |    4 |  32 | 0.457 |   13 |    14 |         0 |  106 |  120 |    3.03 |    3.43 |  14.1 |  80.2 |       8.1 |      82.9 |       30.2 |    29.8 |   45.9 |
| 26 | Edmonton Oilers       | 20232024 |   31 |  15 |  15 | --  |    1 |  31 | 0.5   |   13 |    14 |         1 |  107 |  106 |    3.45 |    3.42 |  26.2 |  78   |      22.3 |      81.7 |       34.2 |    28.4 |   51.8 |
| 27 | Columbus Blue Jackets | 20232024 |   35 |  11 |  18 | --  |    6 |  28 | 0.4   |    9 |    11 |         0 |  108 |  127 |    3.09 |    3.63 |  15.3 |  81.4 |      12.2 |      81.4 |       29.8 |    34.2 |   47.6 |
| 28 | Ottawa Senators       | 20232024 |   29 |  12 |  17 | --  |    0 |  24 | 0.414 |    9 |    11 |         1 |   99 |  103 |    3.41 |    3.55 |  17.7 |  71.3 |      14.3 |      72.3 |       32.5 |    30.7 |   50.6 |
| 29 | Anaheim Ducks         | 20232024 |   33 |  12 |  21 | --  |    0 |  24 | 0.364 |    8 |    11 |         1 |   85 |  111 |    2.58 |    3.36 |  21.7 |  79.9 |      20.8 |      82.6 |       29.3 |    31.8 |   48.5 |
| 30 | Chicago Blackhawks    | 20232024 |   33 |  10 |  22 | --  |    1 |  21 | 0.318 |    8 |    10 |         0 |   80 |  122 |    2.42 |    3.7  |  12.5 |  74.3 |       7.7 |      76.2 |       26.7 |    32.7 |   45.7 |
| 31 | San Jose Sharks       | 20232024 |   34 |   9 |  22 | --  |    3 |  21 | 0.309 |    7 |     9 |         0 |   73 |  137 |    2.15 |    4.03 |  20.2 |  72.9 |      14.6 |      74.6 |       25.7 |    35.6 |   50.7 | 3.09 |  22.1 |  86.4 |      19   |      93.2 |       29.8 |    30.7 |   53.5 |


## Preprocessing

Preprocessing for the data was to remove unnecessary variables and set Team as index. These were
1. Season
2. GP
3. W
4. L
5. T
6. OT
7. P
8. RW
9. ROW
Since they carry no information on how the team plays. For example GP (Games played) only tells about the schedule of that team.

**Data after variable elimination**

| Team                  |    P% |   GF/GP |   GA/GP |   PP% |   PK% |   Net PP% |   Net PK% |   Shots/GP |   SA/GP |   FOW% |
|:----------------------|------:|--------:|--------:|------:|------:|----------:|----------:|-----------:|--------:|-------:|
| Vancouver Canucks     | 0.7   |    3.86 |    2.51 |  24.2 |  77.8 |      24.2 |      81.5 |       28   |    30   |   50.7 |
| New York Rangers      | 0.734 |    3.34 |    2.75 |  31.1 |  85.7 |      27.2 |      87.8 |       30.9 |    29.7 |   54.8 |
| Vegas Golden Knights  | 0.671 |    3.37 |    2.71 |  22.5 |  81   |      21.7 |      85.7 |       32.3 |    30.1 |   49.6 |
| Colorado Avalanche    | 0.647 |    3.65 |    3.03 |  23.6 |  83.3 |      19.7 |      87.5 |       32.2 |    29.4 |   49.2 |
| Dallas Stars          | 0.688 |    3.5  |    3.09 |  22.1 |  86.4 |      19   |      93.2 |       29.8 |    30.7 |   53.5 |
| Boston Bruins         | 0.688 |    3.06 |    2.66 |  24.5 |  85.8 |      22.5 |      85.8 |       31   |    32.3 |   50.3 |
| Winnipeg Jets         | 0.672 |    3.41 |    2.53 |  18.2 |  75   |      16.2 |      78.1 |       31.1 |    28.8 |   47.3 |
| Los Angeles Kings     | 0.7   |    3.53 |    2.37 |  20   |  86.6 |      16.2 |      92.8 |       33.9 |    26.6 |   50.8 |
| New York Islanders    | 0.621 |    3.12 |    3.18 |  24.7 |  71   |      23.7 |      79   |       30.1 |    35.7 |   50.7 |
| Florida Panthers      | 0.606 |    2.91 |    2.61 |  18.9 |  82.9 |      14.2 |      83.8 |       34.3 |    27.1 |   50.3 |
| Philadelphia Flyers   | 0.606 |    2.97 |    2.76 |  10.6 |  85.7 |       8.7 |      92.4 |       32.9 |    28.6 |   46.9 |
| Toronto Maple Leafs   | 0.645 |    3.58 |    3.35 |  26.4 |  79.2 |      22   |      83.3 |       32.6 |    32.5 |   53.2 |
| Tampa Bay Lightning   | 0.557 |    3.34 |    3.43 |  30.4 |  79.6 |      28.6 |      79.6 |       30.4 |    31.1 |   52   |
| Washington Capitals   | 0.629 |    2.39 |    2.68 |  12.4 |  82.7 |      11.2 |      84.7 |       28.1 |    30.7 |   47.3 |
| Nashville Predators   | 0.559 |    3.12 |    3.06 |  20.5 |  77.3 |      18   |      80.9 |       29.8 |    31   |   49.2 |
| Carolina Hurricanes   | 0.559 |    3.24 |    3.18 |  24.4 |  82.7 |      18.3 |      88.2 |       33.9 |    25.6 |   51.2 |
| New Jersey Devils     | 0.563 |    3.41 |    3.56 |  30   |  77.7 |      27   |      79.6 |       31.7 |    29.3 |   53.4 |
| Arizona Coyotes       | 0.545 |    3.06 |    2.88 |  23.2 |  80.2 |      18.8 |      82.2 |       27.1 |    31.3 |   47.5 |
| Detroit Red Wings     | 0.529 |    3.53 |    3.32 |  21.6 |  79.5 |      18   |      82.8 |       30.1 |    32.2 |   48.8 |
| St. Louis Blues       | 0.53  |    3    |    3.33 |  11.6 |  78.9 |       7.4 |      87.8 |       30.7 |    32   |   49.5 |
| Montréal Canadiens    | 0.53  |    2.79 |    3.3  |  17.7 |  73   |      12.6 |      75.7 |       29.3 |    33.6 |   53.9 |
| Pittsburgh Penguins   | 0.531 |    2.84 |    2.78 |  13.7 |  82.7 |       9.8 |      84.6 |       32.9 |    30.9 |   54.7 |
| Minnesota Wild        | 0.531 |    3.03 |    3.16 |  18.2 |  72.2 |      13.6 |      73.9 |       30.2 |    30.3 |   45.3 |
| Calgary Flames        | 0.485 |    3    |    3.26 |  11.8 |  83.3 |       8.2 |      91.7 |       31.6 |    29.8 |   50.4 |
| Seattle Kraken        | 0.471 |    2.69 |    3.09 |  20.8 |  79.2 |      17   |      81.2 |       29.9 |    29.2 |   48.9 |
| Buffalo Sabres        | 0.457 |    3.03 |    3.43 |  14.1 |  80.2 |       8.1 |      82.9 |       30.2 |    29.8 |   45.9 |
| Edmonton Oilers       | 0.5   |    3.45 |    3.42 |  26.2 |  78   |      22.3 |      81.7 |       34.2 |    28.4 |   51.8 |
| Columbus Blue Jackets | 0.4   |    3.09 |    3.63 |  15.3 |  81.4 |      12.2 |      81.4 |       29.8 |    34.2 |   47.6 |
| Ottawa Senators       | 0.414 |    3.41 |    3.55 |  17.7 |  71.3 |      14.3 |      72.3 |       32.5 |    30.7 |   50.6 |
| Anaheim Ducks         | 0.364 |    2.58 |    3.36 |  21.7 |  79.9 |      20.8 |      82.6 |       29.3 |    31.8 |   48.5 |
| Chicago Blackhawks    | 0.318 |    2.42 |    3.7  |  12.5 |  74.3 |       7.7 |      76.2 |       26.7 |    32.7 |   45.7 |
| San Jose Sharks       | 0.309 |    2.15 |    4.03 |  20.2 |  72.9 |      14.6 |      74.6 |       25.7 |    35.6 |   50.7 |


## Clustering
Clustering method was chosen to be K-means since it's a highly flexible and fast clustering method.

### Selection of K
Selection of K was done by plotting inertia for different k-values and finding an "elbow" which means that higher values of k do not bring
significantly more information.

**Inertia to value of K**\
<img src="https://github.com/DaniBarlund/nhl-clustering/blob/main/photos/inertia.png" width="500" height="400">

From the plot value of k was chosen to be 4.
**K=4**

### K-means with K=4

K-means clustering was done using sklearn library with k of 4 and initial value of 10. Results for the cluster were added to the dataframe

**Data with clusters**\
| Team                  |   Cluster |    P% |   GF/GP |   GA/GP |   PP% |   PK% |   Net PP% |   Net PK% |   Shots/GP |   SA/GP |   FOW% |
|:----------------------|----------:|------:|--------:|--------:|------:|------:|----------:|----------:|-----------:|--------:|-------:|
| Vancouver Canucks     |         1 | 0.7   |    3.86 |    2.51 |  24.2 |  77.8 |      24.2 |      81.5 |       28   |    30   |   50.7 |
| New York Rangers      |         1 | 0.734 |    3.34 |    2.75 |  31.1 |  85.7 |      27.2 |      87.8 |       30.9 |    29.7 |   54.8 |
| Vegas Golden Knights  |         0 | 0.671 |    3.37 |    2.71 |  22.5 |  81   |      21.7 |      85.7 |       32.3 |    30.1 |   49.6 |
| Colorado Avalanche    |         0 | 0.647 |    3.65 |    3.03 |  23.6 |  83.3 |      19.7 |      87.5 |       32.2 |    29.4 |   49.2 |
| Dallas Stars          |         0 | 0.688 |    3.5  |    3.09 |  22.1 |  86.4 |      19   |      93.2 |       29.8 |    30.7 |   53.5 |
| Boston Bruins         |         0 | 0.688 |    3.06 |    2.66 |  24.5 |  85.8 |      22.5 |      85.8 |       31   |    32.3 |   50.3 |
| Winnipeg Jets         |         2 | 0.672 |    3.41 |    2.53 |  18.2 |  75   |      16.2 |      78.1 |       31.1 |    28.8 |   47.3 |
| Los Angeles Kings     |         0 | 0.7   |    3.53 |    2.37 |  20   |  86.6 |      16.2 |      92.8 |       33.9 |    26.6 |   50.8 |
| New York Islanders    |         1 | 0.621 |    3.12 |    3.18 |  24.7 |  71   |      23.7 |      79   |       30.1 |    35.7 |   50.7 |
| Florida Panthers      |         0 | 0.606 |    2.91 |    2.61 |  18.9 |  82.9 |      14.2 |      83.8 |       34.3 |    27.1 |   50.3 |
| Philadelphia Flyers   |         3 | 0.606 |    2.97 |    2.76 |  10.6 |  85.7 |       8.7 |      92.4 |       32.9 |    28.6 |   46.9 |
| Toronto Maple Leafs   |         1 | 0.645 |    3.58 |    3.35 |  26.4 |  79.2 |      22   |      83.3 |       32.6 |    32.5 |   53.2 |
| Tampa Bay Lightning   |         1 | 0.557 |    3.34 |    3.43 |  30.4 |  79.6 |      28.6 |      79.6 |       30.4 |    31.1 |   52   |
| Washington Capitals   |         3 | 0.629 |    2.39 |    2.68 |  12.4 |  82.7 |      11.2 |      84.7 |       28.1 |    30.7 |   47.3 |
| Nashville Predators   |         0 | 0.559 |    3.12 |    3.06 |  20.5 |  77.3 |      18   |      80.9 |       29.8 |    31   |   49.2 |
| Carolina Hurricanes   |         0 | 0.559 |    3.24 |    3.18 |  24.4 |  82.7 |      18.3 |      88.2 |       33.9 |    25.6 |   51.2 |
| New Jersey Devils     |         1 | 0.563 |    3.41 |    3.56 |  30   |  77.7 |      27   |      79.6 |       31.7 |    29.3 |   53.4 |
| Arizona Coyotes       |         0 | 0.545 |    3.06 |    2.88 |  23.2 |  80.2 |      18.8 |      82.2 |       27.1 |    31.3 |   47.5 |
| Detroit Red Wings     |         0 | 0.529 |    3.53 |    3.32 |  21.6 |  79.5 |      18   |      82.8 |       30.1 |    32.2 |   48.8 |
| St. Louis Blues       |         3 | 0.53  |    3    |    3.33 |  11.6 |  78.9 |       7.4 |      87.8 |       30.7 |    32   |   49.5 |
| Montréal Canadiens    |         2 | 0.53  |    2.79 |    3.3  |  17.7 |  73   |      12.6 |      75.7 |       29.3 |    33.6 |   53.9 |
| Pittsburgh Penguins   |         3 | 0.531 |    2.84 |    2.78 |  13.7 |  82.7 |       9.8 |      84.6 |       32.9 |    30.9 |   54.7 |
| Minnesota Wild        |         2 | 0.531 |    3.03 |    3.16 |  18.2 |  72.2 |      13.6 |      73.9 |       30.2 |    30.3 |   45.3 |
| Calgary Flames        |         3 | 0.485 |    3    |    3.26 |  11.8 |  83.3 |       8.2 |      91.7 |       31.6 |    29.8 |   50.4 |
| Seattle Kraken        |         0 | 0.471 |    2.69 |    3.09 |  20.8 |  79.2 |      17   |      81.2 |       29.9 |    29.2 |   48.9 |
| Buffalo Sabres        |         3 | 0.457 |    3.03 |    3.43 |  14.1 |  80.2 |       8.1 |      82.9 |       30.2 |    29.8 |   45.9 |
| Edmonton Oilers       |         1 | 0.5   |    3.45 |    3.42 |  26.2 |  78   |      22.3 |      81.7 |       34.2 |    28.4 |   51.8 |
| Columbus Blue Jackets |         3 | 0.4   |    3.09 |    3.63 |  15.3 |  81.4 |      12.2 |      81.4 |       29.8 |    34.2 |   47.6 |
| Ottawa Senators       |         2 | 0.414 |    3.41 |    3.55 |  17.7 |  71.3 |      14.3 |      72.3 |       32.5 |    30.7 |   50.6 |
| Anaheim Ducks         |         0 | 0.364 |    2.58 |    3.36 |  21.7 |  79.9 |      20.8 |      82.6 |       29.3 |    31.8 |   48.5 |
| Chicago Blackhawks    |         2 | 0.318 |    2.42 |    3.7  |  12.5 |  74.3 |       7.7 |      76.2 |       26.7 |    32.7 |   45.7 |
| San Jose Sharks       |         2 | 0.309 |    2.15 |    4.03 |  20.2 |  72.9 |      14.6 |      74.6 |       25.7 |    35.6 |   50.7 |


To make understanding of the clusters they were plotted to teams rank in the standings.

**Cluster on the team rank**\
<img src="https://github.com/DaniBarlund/nhl-clustering/blob/main/photos/clusterForRank.png" width="500" height="400">

From the plot above it can be seen that in cluster 0 and 3 teams are from very similar rankings. Where as clusters 1 and 2 are more evenly spread around the rankings.

## Finding the most similar team using NearestNeighbor search
Idea was to find for each team a team that is most similar to them. This could be helpful if a customer likes to watch Minnesota Wild
but they are not playing today so the most similar team could be suggested instead.

NearestNeigbor was found by using sklearns NearestNeigbors functions using number of neighbors of 2 to find itself and the closest one.
Algorithm for the search was set to "auto" and distance used was eucledian distance.

These closest teams and the distance to them were added to the data.

**Data with closest team and distance**\
| Team                  |   Cluster | Closest team         |   Closest Distance |    P% |   GF/GP |   GA/GP |   PP% |   PK% |   Net PP% |   Net PK% |   Shots/GP |   SA/GP |   FOW% |
|:----------------------|----------:|:---------------------|-------------------:|------:|--------:|--------:|------:|------:|----------:|----------:|-----------:|--------:|-------:|
| Vancouver Canucks     |         1 | Anaheim Ducks        |            6.05589 | 0.7   |    3.86 |    2.51 |  24.2 |  77.8 |      24.2 |      81.5 |       28   |    30   |   50.7 |
| New York Rangers      |         1 | Boston Bruins        |            9.8878  | 0.734 |    3.34 |    2.75 |  31.1 |  85.7 |      27.2 |      87.8 |       30.9 |    29.7 |   54.8 |
| Vegas Golden Knights  |         0 | Colorado Avalanche   |            3.81856 | 0.671 |    3.37 |    2.71 |  22.5 |  81   |      21.7 |      85.7 |       32.3 |    30.1 |   49.6 |
| Colorado Avalanche    |         0 | Vegas Golden Knights |            3.81856 | 0.647 |    3.65 |    3.03 |  23.6 |  83.3 |      19.7 |      87.5 |       32.2 |    29.4 |   49.2 |
| Dallas Stars          |         0 | Los Angeles Kings    |            7.34026 | 0.688 |    3.5  |    3.09 |  22.1 |  86.4 |      19   |      93.2 |       29.8 |    30.7 |   53.5 |
| Boston Bruins         |         0 | Colorado Avalanche   |            5.41633 | 0.688 |    3.06 |    2.66 |  24.5 |  85.8 |      22.5 |      85.8 |       31   |    32.3 |   50.3 |
| Winnipeg Jets         |         2 | Nashville Predators  |            6.0148  | 0.672 |    3.41 |    2.53 |  18.2 |  75   |      16.2 |      78.1 |       31.1 |    28.8 |   47.3 |
| Los Angeles Kings     |         0 | Dallas Stars         |            7.34026 | 0.7   |    3.53 |    2.37 |  20   |  86.6 |      16.2 |      92.8 |       33.9 |    26.6 |   50.8 |
| New York Islanders    |         1 | Vancouver Canucks    |            9.53377 | 0.621 |    3.12 |    3.18 |  24.7 |  71   |      23.7 |      79   |       30.1 |    35.7 |   50.7 |
| Florida Panthers      |         0 | Seattle Kraken       |            7.61098 | 0.606 |    2.91 |    2.61 |  18.9 |  82.9 |      14.2 |      83.8 |       34.3 |    27.1 |   50.3 |
| Philadelphia Flyers   |         3 | Calgary Flames       |            4.85649 | 0.606 |    2.97 |    2.76 |  10.6 |  85.7 |       8.7 |      92.4 |       32.9 |    28.6 |   46.9 |
| Toronto Maple Leafs   |         1 | Edmonton Oilers      |            5.05003 | 0.645 |    3.58 |    3.35 |  26.4 |  79.2 |      22   |      83.3 |       32.6 |    32.5 |   53.2 |
| Tampa Bay Lightning   |         1 | New Jersey Devils    |            3.63893 | 0.557 |    3.34 |    3.43 |  30.4 |  79.6 |      28.6 |      79.6 |       30.4 |    31.1 |   52   |
| Washington Capitals   |         3 | Buffalo Sabres       |            5.49288 | 0.629 |    2.39 |    2.68 |  12.4 |  82.7 |      11.2 |      84.7 |       28.1 |    30.7 |   47.3 |
| Nashville Predators   |         0 | Seattle Kraken       |            2.88506 | 0.559 |    3.12 |    3.06 |  20.5 |  77.3 |      18   |      80.9 |       29.8 |    31   |   49.2 |
| Carolina Hurricanes   |         0 | Colorado Avalanche   |            4.99783 | 0.559 |    3.24 |    3.18 |  24.4 |  82.7 |      18.3 |      88.2 |       33.9 |    25.6 |   51.2 |
| New Jersey Devils     |         1 | Tampa Bay Lightning  |            3.63893 | 0.563 |    3.41 |    3.56 |  30   |  77.7 |      27   |      79.6 |       31.7 |    29.3 |   53.4 |
| Arizona Coyotes       |         0 | Anaheim Ducks        |            3.61712 | 0.545 |    3.06 |    2.88 |  23.2 |  80.2 |      18.8 |      82.2 |       27.1 |    31.3 |   47.5 |
| Detroit Red Wings     |         0 | Anaheim Ducks        |            3.14187 | 0.529 |    3.53 |    3.32 |  21.6 |  79.5 |      18   |      82.8 |       30.1 |    32.2 |   48.8 |
| St. Louis Blues       |         3 | Calgary Flames       |            6.45886 | 0.53  |    3    |    3.33 |  11.6 |  78.9 |       7.4 |      87.8 |       30.7 |    32   |   49.5 |
| Montréal Canadiens    |         2 | San Jose Sharks      |            6.29773 | 0.53  |    2.79 |    3.3  |  17.7 |  73   |      12.6 |      75.7 |       29.3 |    33.6 |   53.9 |
| Pittsburgh Penguins   |         3 | St. Louis Blues      |            8.26245 | 0.531 |    2.84 |    2.78 |  13.7 |  82.7 |       9.8 |      84.6 |       32.9 |    30.9 |   54.7 |
| Minnesota Wild        |         2 | Ottawa Senators      |            6.16118 | 0.531 |    3.03 |    3.16 |  18.2 |  72.2 |      13.6 |      73.9 |       30.2 |    30.3 |   45.3 |
| Calgary Flames        |         3 | Philadelphia Flyers  |            4.85649 | 0.485 |    3    |    3.26 |  11.8 |  83.3 |       8.2 |      91.7 |       31.6 |    29.8 |   50.4 |
| Seattle Kraken        |         0 | Nashville Predators  |            2.88506 | 0.471 |    2.69 |    3.09 |  20.8 |  79.2 |      17   |      81.2 |       29.9 |    29.2 |   48.9 |
| Buffalo Sabres        |         3 | Washington Capitals  |            5.49288 | 0.457 |    3.03 |    3.43 |  14.1 |  80.2 |       8.1 |      82.9 |       30.2 |    29.8 |   45.9 |
| Edmonton Oilers       |         1 | Toronto Maple Leafs  |            5.05003 | 0.5   |    3.45 |    3.42 |  26.2 |  78   |      22.3 |      81.7 |       34.2 |    28.4 |   51.8 |
| Columbus Blue Jackets |         3 | Washington Capitals  |            6.21811 | 0.4   |    3.09 |    3.63 |  15.3 |  81.4 |      12.2 |      81.4 |       29.8 |    34.2 |   47.6 |
| Ottawa Senators       |         2 | Minnesota Wild       |            6.16118 | 0.414 |    3.41 |    3.55 |  17.7 |  71.3 |      14.3 |      72.3 |       32.5 |    30.7 |   50.6 |
| Anaheim Ducks         |         0 | Detroit Red Wings    |            3.14187 | 0.364 |    2.58 |    3.36 |  21.7 |  79.9 |      20.8 |      82.6 |       29.3 |    31.8 |   48.5 |
| Chicago Blackhawks    |         2 | Minnesota Wild       |            9.79179 | 0.318 |    2.42 |    3.7  |  12.5 |  74.3 |       7.7 |      76.2 |       26.7 |    32.7 |   45.7 |
| San Jose Sharks       |         2 | Montréal Canadiens   |            6.29773 | 0.309 |    2.15 |    4.03 |  20.2 |  72.9 |      14.6 |      74.6 |       25.7 |    35.6 |   50.7 |

### Finding teams with the highest average goals for and against.

Finding the teams was done by selecting the cluster with the highest total goals (sum of goals for and against). Average goals was calculated
using groupBy on cluster and then taking the mean for goals.

**Average goals per game**\
<img src="https://github.com/DaniBarlund/nhl-clustering/blob/main/photos/goalsForCluster.png" width="500" height="400">

From the plot it is clear that cluster 1 has highest average total goals per game. Teams in that cluster can be seen below.

| Team                |   Cluster | Closest team        |   Closest Distance |    P% |   GF/GP |   GA/GP |   PP% |   PK% |   Net PP% |   Net PK% |   Shots/GP |   SA/GP |   FOW% |
|:--------------------|----------:|:--------------------|-------------------:|------:|--------:|--------:|------:|------:|----------:|----------:|-----------:|--------:|-------:|
| Vancouver Canucks   |         1 | Anaheim Ducks       |            6.05589 | 0.7   |    3.86 |    2.51 |  24.2 |  77.8 |      24.2 |      81.5 |       28   |    30   |   50.7 |
| New York Rangers    |         1 | Boston Bruins       |            9.8878  | 0.734 |    3.34 |    2.75 |  31.1 |  85.7 |      27.2 |      87.8 |       30.9 |    29.7 |   54.8 |
| New York Islanders  |         1 | Vancouver Canucks   |            9.53377 | 0.621 |    3.12 |    3.18 |  24.7 |  71   |      23.7 |      79   |       30.1 |    35.7 |   50.7 |
| Toronto Maple Leafs |         1 | Edmonton Oilers     |            5.05003 | 0.645 |    3.58 |    3.35 |  26.4 |  79.2 |      22   |      83.3 |       32.6 |    32.5 |   53.2 |
| Tampa Bay Lightning |         1 | New Jersey Devils   |            3.63893 | 0.557 |    3.34 |    3.43 |  30.4 |  79.6 |      28.6 |      79.6 |       30.4 |    31.1 |   52   |
| New Jersey Devils   |         1 | Tampa Bay Lightning |            3.63893 | 0.563 |    3.41 |    3.56 |  30   |  77.7 |      27   |      79.6 |       31.7 |    29.3 |   53.4 |
| Edmonton Oilers     |         1 | Toronto Maple Leafs |            5.05003 | 0.5   |    3.45 |    3.42 |  26.2 |  78   |      22.3 |      81.7 |       34.2 |    28.4 |   51.8 |

## Conclusion

Clustering and search methods and algorithms can be used on various tasks. On this project they were only used for what they are
designed to do but during research I found multiple other use cases. For example nearestNeighbor can also be used for classification
or to find outliers in data. But overall an positive learning experience from whichs results I will benefit from next time my favourite 
NHL team doesn't play.
