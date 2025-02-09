import matplotlib as plt
import seaborn as sns

def boxplot(series, title = 'Title', label=None):
  if not label:
    label = series.name
  sns.boxplot(y=series)
  plt.title(title)
  plt.ylabel(label)
  plt.ticklabel_format(style='plain', axis='y')
  plt.grid(True, linestyle='--', alpha=0.7)
  plt.show()
  plt.close()
