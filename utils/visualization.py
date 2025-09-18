import matplotlib.pyplot as plt

def plot_hist(df, column):
    df[column].hist()
    plt.show()
