import numpy as np

def calculate(list):
  if(len(list)!=9):
    raise ValueError("List must contain nine numbers.")
  listReshaped = np.reshape(list, (3,3)).tolist()
  calculations = {"mean": [np.mean(listReshaped, axis=0).tolist(), np.mean(listReshaped, axis=1).tolist(), np.mean(list)],
                  "variance": [np.var(listReshaped, axis=0).tolist(), np.var(listReshaped, axis=1).tolist(), np.var(list)],
                  "standard deviation": [np.std(listReshaped, axis=0).tolist(), np.std(listReshaped, axis=1).tolist(), np.std(list)],
                  "max" : [np.max(listReshaped, axis=0).tolist(), np.max(listReshaped, axis=1).tolist(), np.max(list)],
                  "min" : [np.min(listReshaped, axis=0).tolist(), np.min(listReshaped, axis=1).tolist(), np.min(list)],
                  "sum" : [np.sum(listReshaped, axis=0).tolist(), np.sum(listReshaped, axis=1).tolist(), np.sum(list)]}



  return calculations