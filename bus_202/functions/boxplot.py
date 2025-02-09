import matplotlib.pyplot as plt

def boxplot(series, title='Title', label=None):
  plt.figure()
  if not label:
    label = series.name
  
  # Create boxplot with matplotlib
  plt.boxplot(series,
    patch_artist=True,  # Fill boxes with color
    boxprops=dict(facecolor='skyblue', color='black'),  # Box style
    medianprops=dict(color='black'),  # Median line style
    flierprops=dict(marker='o', markerfacecolor='gray'),  # Outlier style
    whiskerprops=dict(color='black'),  # Whisker style
    capprops=dict(color='black'))  # Cap style
  
  plt.title(title)
  plt.ylabel(label)
  plt.ticklabel_format(style='plain', axis='y')
  plt.grid(True, linestyle='--', alpha=0.7)
  
  plt.show(block=False)
