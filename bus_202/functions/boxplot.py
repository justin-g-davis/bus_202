import matplotlib.pyplot as plt

def boxplot(series, title='Title', label=None):
  # Create figure and axis
  fig, ax = plt.subplots()
  
  if not label:
    label = series.name
  
  # Create boxplot on the axis
  ax.boxplot(series,
  patch_artist=True,  # Fill boxes
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
