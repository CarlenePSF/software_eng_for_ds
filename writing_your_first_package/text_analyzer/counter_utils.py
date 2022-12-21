# Import needed functionality
from collections import Counter


def plot_counter(counter, n_most_common=5):
    """

    :param counter:
    :param n_most_common:
    :return:
    """
    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    plot_counter_most_common(top_items)


def sum_counters(counters):
    """

    :param counters:
    :return:
    """
    # Sum the inputted counters
    return sum(counters, Counter())
