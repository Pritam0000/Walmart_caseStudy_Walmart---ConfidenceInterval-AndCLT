import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    figs = []

    # Purchase distribution by gender
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='Purchase', hue='Gender', kde=True, ax=ax)
    ax.set_title("Purchase Distribution by Gender")
    figs.append(fig)

    # Average purchase amount by gender
    fig, ax = plt.subplots(figsize=(8, 6))
    df.groupby('Gender')['Purchase'].mean().plot(kind='bar', ax=ax)
    ax.set_title("Average Purchase Amount by Gender")
    ax.set_ylabel("Average Purchase Amount")
    figs.append(fig)

    return figs