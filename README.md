# Test_Metrics
Short code for creating student-results tables and performing simple statistics.

The code assumes the test consists of 5 problems. The code searches 
for JMBAG numbers from a separate table (jmbags.txt) and adds these
values to the corresponding names. We also include the possibility
of adding bonus points (homework and such) from a separate table
(bonus.txt). Default values are zero if any of these are missing.

The code creates also a statistical analysis of the results and
plots 4 graphs.
1) Mean problem points
2) Pie chart pass vs fail
3) Student results distribution (and comparison with a Gaussian)
4) Cumulative pass ratio. For this we include data from earlier tests (cumulative_stat.txt)

The code requires a folder titled 'Input' that contains:
1) results.txt
2) jmbags.txt
3) bonus.txt
4) cumulative_stat.txt

We give an example of these in the repository. We also give an example of 
graph-output.
