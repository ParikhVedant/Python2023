import matplotlib.pyplot as plt


def plot_bar_graph_from_python_dict(frequency: dict) -> None:
    """
        Plots a bar graph from a python dict. 

        X axis: dict keys 
        Y axis: dict values 
    """

    # creating the dataset
    x_axis = list(frequency.keys())
    y_axis = list(frequency.values())

    # creating the bar plot
    plt.bar(x_axis, y_axis)

    plt.show()
