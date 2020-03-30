import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd

data_8192 = pd.read_csv("expectiminmax_scores_8192.csv")
data_2048 = pd.read_csv("expectiminmax_scores_2048.csv")
data_1000_moves = pd.read_csv("expectiminmax_score_1000_moves.csv")


plt.plot(data_8192["Move"], data_8192["Score"], color = "red", label="8192")
plt.plot(data_2048["Move"], data_2048["Score"], color="blue", label="2048")
plt.plot(data_1000_moves["Move"], data_1000_moves["Score"], color="green", label="1000 Moves")

plt.legend(loc="upper left")
plt.title("2048: Moves Vs. Score")
plt.xlabel("moves")
plt.ylabel("score")
plt.savefig('Graph_Comparison_Final.png')


