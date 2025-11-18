import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def plot_heatmap():
    data = np.random.rand(6,6)
    sb.heatmap(data,annot=True, cmap="viridis")
    plt.show()


def interactive_heatmap():
    data = np.random.rand(6,6)
    df = pd.DataFrame(data, columns=[f"C{i}" for i in range(6)], index=[f"R{i}" for i in range(6)])
    fig = px.imshow(df, text_auto=True, color_continuous_scale="viridis")
    fig.show()


plot_heatmap()
interactive_heatmap()