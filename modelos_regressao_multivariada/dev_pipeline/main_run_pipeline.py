import pandas as pd
from utils.data_viz import (plot_histogram,
                            hist_one_variable,
                            frequency_plot_categorical)

house_dataset = pd.read_csv('data/housing.csv')
data = house_dataset.copy()

target = 'median_house_value',
features = list(house_dataset.drop(target, axis=1).columns)

print('Variável alvo: ', target)
print('Caracteristicas: ', features)


def main():
    plot_histogram(data)
    hist_one_variable(data, target)
    frequency_plot_categorical(data, 'ocean_proximity')


if __name__ == '__main__':
    main()
