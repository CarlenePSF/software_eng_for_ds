"""
# ----- Fist way to import the package -----
# import utils submodule
import my_package.utils

# print a description of the package
print(help(my_package))

# Decide to start seeing other people
my_package.utils.we_need_to_talk(break_up=True)

# ----- Second way of import a package -----
from my_package import utils

utils.we_need_to_talk(break_up=True)

# ----- third way of import a package -----
from my_package.utils import we_need_to_talk

we_need_to_talk(break_up=True)
"""
# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = ____.____(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
____.____(word_count_totals)
