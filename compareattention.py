import pandas as pd 
import pickle
import numpy as np

attn_df = pd.read_pickle("./AttnDF/IntroOnly1_attn_xbn.pkl")


pred_weights = [] 
source_weights = []

rand_mtrx = np.random.rand(len(attn_df.index), len(attn_df.columns))
rand_attn_matrix = rand_mtrx / rand_mtrx.sum(axis=1)[:, np.newaxis]

rand_attn_df = pd.DataFrame(rand_attn_matrix, columns=attn_df.columns, index=attn_df.index)
print(rand_attn_df.head())

rand_pred_weights = []
rand_source_weights = []

for i in range(0, len(attn_df.index)):
  for j in range(0,len(attn_df.columns)):
    if attn_df.index[i] == attn_df.columns[j]:
      print(i,j)
      print("attn matrix : === ",attn_df.iloc[i].iat[j])
      print("Random matrix: =============",rand_attn_df.iloc[i].iat[j])
      pred_weights.append(attn_df.iloc[i].iat[j])
      rand_pred_weights.append(rand_attn_df.iloc[i].iat[j])
    else:
      source_weights.append(attn_df.iloc[i].iat[j])
      rand_source_weights.append(rand_attn_df.iloc[i].iat[j])

print("Actual Attention Weights")
print("pred_weights:  ", sum(pred_weights))
print("other_weights: ", sum(source_weights))

print("Random Weights")
print("rand_pred_weights: ", sum(rand_pred_weights))
print("rand_source_weights: ", sum(rand_source_weights))
