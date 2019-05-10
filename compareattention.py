import pandas as pd 
import pickle

attn_df = pd.read_pickle("./AttnDF/attn_0.pkl")


pred_weights = [] 
source_weights = []


for i in range(0, len(attn_df.index)):
  for j in range(0,len(attn_df.columns)):
    if attn_df.index[i] == attn_df.columns[j]:
      print(i,j)
      print(attn_df.iloc[i].iat[j])
      pred_weights.append(attn_df.iloc[i].iat[j])
    else:
      source_weights.append(attn_df.iloc[i].iat[j])

print("pred_weights:  ", sum(pred_weights))
print("other_weights: ", sum(source_weights))
