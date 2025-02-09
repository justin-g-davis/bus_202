import matplotlib.pyplot as plt
import numpy as np

def boxplot(series, title='Title', label=None):
  # Create figure and axis
  fig, ax = plt.subplots()
  
  if not label:
    label = series.name
  
  # Convert to numpy array and ensure 1D
  data = np.array(series.dropna()).flatten()
  
  # Print debug info
  print(f"Shape of data: {data.shape}")
  print(f"First few values: {data[:5]}")
  
  # Create boxplot on the axis
  ax.boxplot(data,
  patch_artist=True,
  boxprops=dict(facecolor='skyblue', color='black'),
  medianprops=dict(color='black'),
  flierprops=dict(marker='o', markerfacecolor='gray'),
  whiskerprops=dict(color='black'),
  capprops=dict(color='black'))
  
  # Add labels and styling
  ax.set_title(title)
  ax.set_ylabel(label)
  ax.ticklabel_format(style='plain', axis='y')
  ax.grid(True, linestyle='--', alpha=0.7)
  
  plt.show(block=False)
