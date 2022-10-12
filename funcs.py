import numpy as np
import pandas as pd
import plotly.graph_objects as go

def compile_data(data, sample="s12345"):
  # preprocess dataframe
  s1_t1 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 2"]].to_numpy().astype(float)
  s1_t2 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 3"]].to_numpy().astype(float)
  s1_t3 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 4"]].to_numpy().astype(float)
  s2_t1 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 8"]].to_numpy().astype(float)
  s2_t2 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 9"]].to_numpy().astype(float)
  s2_t3 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 10"]].to_numpy().astype(float)
  s3_t1 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 14"]].to_numpy().astype(float)
  s3_t2 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 15"]].to_numpy().astype(float)
  s3_t3 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 16"]].to_numpy().astype(float)
  s4_t1 = data[["Sample 4 (130nm)", "Unnamed: 20", "Unnamed: 21"]].to_numpy().astype(float)
  s4_t2 = data[["Sample 4 (130nm)", "Unnamed: 20", "Unnamed: 22"]].to_numpy().astype(float)
  s5_t1 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 26"]].to_numpy().astype(float)
  s5_t2 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 27"]].to_numpy().astype(float)
  s5_t3 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 28"]].to_numpy().astype(float)
  
  if sample=="s12345":
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0],s4_t1[:,0], s4_t2[:,0], s5_t1[:,0], s5_t2[:,0], s5_t3[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1],s4_t1[:,1], s4_t2[:,1], s5_t1[:,1], s5_t2[:,1], s5_t3[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2],s4_t1[:,2], s4_t2[:,2], s5_t1[:,2], s5_t2[:,2], s5_t3[:,2]))
    
  if sample=="s1234":
    # Samples 1,2,3,4
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0],s4_t1[:,0], s4_t2[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1],s4_t1[:,1], s4_t2[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2],s4_t1[:,2], s4_t2[:,2]))
    s1_end = s1_t1.shape[0]+s1_t2.shape[0]+s1_t3.shape[0]
    s2_end = s1_end+s2_t1.shape[0]+s2_t2.shape[0]+s2_t3.shape[0]
    s3_end = s2_end+s3_t1.shape[0]+s3_t2.shape[0]+s3_t3.shape[0]
    s4_end = s3_end+s4_t1.shape[0]+s4_t2.shape[0]
    
  if sample=="s123":
    # Samples 1,2,3
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2]))
    s1_end = s1_t1.shape[0]+s1_t2.shape[0]+s1_t3.shape[0]
    s2_end = s1_end+s2_t1.shape[0]+s2_t2.shape[0]+s2_t3.shape[0]
    s3_end = s2_end+s3_t1.shape[0]+s3_t2.shape[0]+s3_t3.shape[0]
    
  if sample=="s4":
    # Sample 4
    temp = np.concatenate((s4_t1[:,0], s4_t2[:,0]))
    hum = np.concatenate((s4_t1[:,1], s4_t2[:,1]))
    thick = np.concatenate((s4_t1[:,2], s4_t2[:,2]))
    s3_end = 0
    s4_end = s3_end+s4_t1.shape[0]+s4_t2.shape[0]
    
  if sample=="s5":
    # Sample 5
    temp = np.concatenate((s5_t1[:,0], s5_t2[:,0], s5_t3[:,0]))
    hum = np.concatenate((s5_t1[:,1], s5_t2[:,1], s5_t3[:,1]))
    thick = np.concatenate((s5_t1[:,2], s5_t2[:,2], s5_t3[:,2]))
    s4_end = 0
  
  s1_end = s1_t1.shape[0]+s1_t2.shape[0]+s1_t3.shape[0]
  s2_end = s1_end+s2_t1.shape[0]+s2_t2.shape[0]+s2_t3.shape[0]
  s3_end = s2_end+s3_t1.shape[0]+s3_t2.shape[0]+s3_t3.shape[0]
  s4_end = s3_end+s4_t1.shape[0]+s4_t2.shape[0]
  s5_end = s4_end+s5_t1.shape[0]+s5_t2.shape[0]+s5_t3.shape[0]
  indices = (s1_end,s2_end,s3_end,s4_end,s5_end)
    
  return temp, hum, thick, indices

    
