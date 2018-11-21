------------------------------------------------------------------------------------------------
# Question

Pedro set up an Internet site to sell figurines from the Brazilian Championship album.
He is organizing a catalog with sets of figurines to sell. Each
Set of cards is formed by 5 cards, one at a time that it has
(Botafogo, Flamengo, Fluminense, Vasco and São Paulo). Two sets
of cards are considered to be distinct if there is at least one card that is in a
it is not without another set. Pedro wants to expose only the most expensive places.
The value of a set is a sum of the values of each figurine that is in it. Its function is
informing the sum of the values of the k distinct sets of more expensive cards. In case
of tie between more expensive sets, of Pedro tied.

# Input
The input is given by a text file called "input.txt". This file has 6 lines:
The first line contains an integer B (5 ≤ B ≤ 10), representing that Peter has B types
different Botafogo figurines, followed by B integers Xi (1 ≤ Xi ≤ 20), representing the
values ​​of each team of this team. The second line contains an integer F (5 ≤ F ≤ 10),
representing that Pedro has F different types of Flamengo figurines, followed by F
integers Xi (1 ≤ Xi ≤ 20), representing the values ​​of each Flemish figurine. The third
line contains an integer L (5 ≤ L ≤ 10), representing that Peter has L different types of
Fluminense figurines, followed by L integers Xi (1 ≤ Xi ≤ 20), representing the values ​​of
each Fluminense figurine. The fourth line contains an integer V (5 ≤ V ≤ 10), representing
that Peter has V different types of figurines from that team, followed by V integers Xi (1 ≤ Xi ≤
20), representing the values ​​of each Vasco figurine. The fifth line contains an integer S (5
≤ S ≤ 10), representing that Pedro has S different types of São Paulo figurines, followed by
by S integers Xi (1 ≤ Xi ≤ 20), representing the values ​​of each figurine of that team. The sixth
line contains an integer K (1 ≤ K ≤ B × F × L × V × S), representing the number of sets
different types of figurines that the catalog of figurines

# Output
Your program should print on the standard output the value of the sum of the values of the K sets
distinct from more expensive figurines.

╔═════════╦════════════════════╦═════╗
║ In      ║ ex1.txt            ║ Out ║
╠═════════╬════════════════════╬═════╣
║ ex1.txt ║ 5 2 5 6 3 8        ║ 413 ║
║         ║ 6 9 6 3 1 5 3      ║     ║
║         ║ 5 4 8 5 2 6        ║     ║
║         ║ 8 3 2 4 9 5 9 10 1 ║     ║
║         ║ 5 7 8 5 1 4        ║     ║
║         ║ 10                 ║     ║
╚═════════╩════════════════════╩═════╝
------------------------------------------------------------------------------------------------
