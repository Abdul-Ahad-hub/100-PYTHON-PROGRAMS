import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv(r"C:\Users\Abdul Ahad\Downloads\dummy_people.csv")


def filter_old():
    return file[file['Age'] > 30]


def plot_graph():
    filtered = filter_old()
    plt.bar(filtered['Name'], filtered['Age'])
    plt.xlabel("Name")
    plt.ylabel("Age")
    plt.title("Result test")
    plt.show()


plot_graph()