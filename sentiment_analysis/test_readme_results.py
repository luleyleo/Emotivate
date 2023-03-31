import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import math

raw_results = {
    'api': {'true_1': 796, 'false_1': 203, 'true_3': 1172, 'false_3': 549},
    'go': {'true_1': 668, 'false_1': 331, 'true_3': 1351, 'false_3': 370}
}

absolute_results = {
    'api': {
        'positive': {
            True: 796,
            False: 203,
        },
        'negative': {
            True: 1172,
            False: 549,
        }
    },
    'go': {
        'positive': {
            True: 668,
            False: 331,
        },
        'negative': {
            True: 1351,
            False: 370,
        }
    }
}

total_positive = 796 + 203
total_negative = 1172 + 549
factor = total_positive / total_negative
total_negative = math.floor(total_negative * factor)

total_examples = total_positive + total_negative

results = {
    'api': {
        'positive': {
            True: 796,
            False: 203,
        },
        'negative': {
            True: math.floor(1172 * factor),
            False: math.ceil(549 * factor),
        }
    },
    'go': {
        'positive': {
            True: 668,
            False: 331,
        },
        'negative': {
            True: math.floor(1351 * factor),
            False: math.ceil(370 * factor),
        }
    }
}

api_table = [
    [results['api']['positive'][True], results['api']['positive'][False]],
    [results['api']['negative'][False], results['api']['negative'][True]],
]

go_table = [
    [results['go']['positive'][True], results['go']['positive'][False]],
    [results['go']['negative'][False], results['go']['negative'][True]],
]


def main():
    figure, axis = plt.subplots(1, 2)
    figure.set_size_inches(12, 5)

    axis[0].set_title('API')
    api_df = pd.DataFrame(api_table, index = ['+', '-'], columns = ['+', '-'])
    sn.heatmap(api_df, fmt='', annot=True, cmap='Blues', ax=axis[0])

    axis[1].set_title('GoEmotions')
    go_df = pd.DataFrame(go_table, index = ['+', '-'], columns = ['+', '-'])
    sn.heatmap(go_df, fmt='', annot=True, cmap='Blues', ax=axis[1])

    figure.savefig('data/plots/confusion.png')


if __name__ == '__main__':
    main()
