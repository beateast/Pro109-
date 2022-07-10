import csv
import pandas as pd
import statistics

df = pd.read_csv("math score")
math_score_list = df["math score"].tolist

math_score_mean = statistics.mean(math_score_list)

math_score_mode = statistics.mode(math_score_list)

math_score_median = statistics.median(math_score_list)

math_score_std_deviation = statistics.stdev(math_score_list)

print("Mean, median, mode and standard deviation are:", math_score_mean, math_score_median, math_score_mode, math_score_std_deviation)

first_std_deviation_start, first_std_deviation_end = math_score_mean.std_deviation, statistics.mean+ statistics.std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

print("{}% of data for math score lies within 1 standard deviation".format(len(first_std_deviation_start)*100.0/len(height_list)))
print("{}% of data for math score lies within 2 standard deviations".format(len(second_std_deviation_start)*100.0/len(height_list)))
print("{}% of data for math score lies within 3 standard deviations".format(len(third_std_deviation_start)*100.0/len(math_score_list)))


