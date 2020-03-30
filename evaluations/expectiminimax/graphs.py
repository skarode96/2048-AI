import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd

data8192 = pd.read_csv("expectiminmax_scores_8192.csv")
data2048 = pd.read_csv("expectiminmax_scores_2048.csv")


plt.plot(data8192["Move"], data8192["Score"], color = "red", label="8192")
plt.plot(data2048["Move"], data2048["Score"], color="blue", label="2048")
plt.legend(loc="upper left")
plt.title("2048: Moves Vs. Score")
plt.xlabel("moves")
plt.ylabel("score")
plt.savefig('Graph_Comparison.png')


