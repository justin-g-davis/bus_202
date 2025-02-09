import matplotlib.pyplot as plt
import seaborn as sns

def histogram(series, title='Title', label=None, bins=30):
  plt.figure()
  if not label:
    label = series.name
  
  # Create histogram with KDE
  sns.histplot(series, bins=bins, kde=True)
  
  # Add labels and grid
  plt.title(title)
  plt.xlabel(label)
  plt.ylabel('Count')
  plt.ticklabel_format(style='plain', axis='x')
  plt.grid(True, linestyle='--', alpha=0.7)
  
  plt.show(block=False)
