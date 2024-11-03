import collections
import random

import matplotlib.pyplot as plt

if __name__ == "__main__":

    N = 100000

    sums_counter = collections.Counter()

    for _ in range(N):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_dice = die1 + die2
        sums_counter[sum_dice] += 1

    probabilities = {sum_dice: count / N for sum_dice, count in sums_counter.items()}

    analytical_probabilities = {
        2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36,
        7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36
    }

    print("Ймовірності методом Монте-Карло:")
    for sum_dice in range(2, 13):
        print(f"Сума {sum_dice}: {probabilities.get(sum_dice, 0):.4f}")

    print("\nАналітичні ймовірності:")
    for sum_dice, prob in analytical_probabilities.items():
        print(f"Сума {sum_dice}: {prob:.4f}")

    fig, ax = plt.subplots()

    sums = range(2, 13)
    monte_carlo_probs = [probabilities.get(sum_dice, 0) for sum_dice in sums]
    analytical_probs = [analytical_probabilities.get(sum_dice, 0) for sum_dice in sums]

    ax.bar(sums, monte_carlo_probs, width=0.4, label='Монте-Карло', align='center')
    ax.plot(sums, analytical_probs, color='red', marker='o', linestyle='-', label='Аналітичні ймовірності')

    ax.set_xlabel('Сума чисел на двох кубиках')
    ax.set_ylabel('Ймовірність')
    ax.set_title('Ймовірності сум на двох кубиках')
    ax.legend()

    plt.show()
