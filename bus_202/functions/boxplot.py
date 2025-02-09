import matplotlib.pyplot as plt
import numpy as np

def boxplot(series, title='Title', label=None):
  plt.figure()
  if not label:
    label = series.name
  
  # Clean data - remove NaN values
  clean_data = series.dropna()
  
  # Convert to numpy array and reshape for boxplot
  data = np.array(clean_data).reshape(-1, 1)
  
  # Create boxplot with matplotlib
  plt.boxplot(data,
  patch_artist=True,
  boxprops=dict(facecolor='skyblue', color='black'),
  medianprops=dict(color='black'),
  flierprops=dict(marker='o', markerfacecolor='gray'),
  whiskerprops=dict(color='black'),
  capprops=dict(color='black'))
  
  plt.title(title)
  plt.ylabel(label)
  plt.ticklabel_format(style='plain', axis='y')
  plt.grid(True, linestyle='--', alpha=0.7)
  
  # Add some debug info
  print(f"Number of valid values: {len(clean_data)}")
  print(f"Data range: {clean_data.min():.1f} to {clean_data.max():.1f}")
  
  plt.show(block=False)
