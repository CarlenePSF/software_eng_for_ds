import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_histogram(df):
    """
    plot a histogram for each feature of the whole dataframe
    :param df:
    :return:
    """
    df.hist(bins=60, figsize=(15, 10))
    plt.show()


def hist_one_variable(df, variable):
    """
    plot a histogram of one specified variable
    :param df:
    :param variable:
    :return: None
    """
    plt.figure(figsize=(8, 6))
    plt.hist(df[variable], bins=50, ec='black', color='#0097A7')
    plt.xlabel(variable, size=15)
    plt.show()


def frequency_plot_categorical(df, categorical_variable):
    """
    plot a frequency bar plot for categorical variables
    :param df:
    :param categorical_variable:
    :return:
    """
    frequency2 = df[categorical_variable].value_counts()

    plt.figure(figsize=(8, 6))
    plt.bar(
        frequency2.index,
        height=frequency2, width=0.10, ec='black'
    )
    plt.xlabel(categorical_variable, size=15)
    plt.show()
