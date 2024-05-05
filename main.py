import matplotlib.pyplot as plt
from functools import lru_cache
from typing import (Callable, Union)
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("--min", type=int, default=-50, help=f"Minimum number in a range of x. (defalut: -50)")
parser.add_argument("--max", type=int, default=50, help=f"Maximum number in a range of x. (defalut: 50)")
parser.add_argument("--dir", type=str, default="./out", help=f"Directory where the figure will be saved. (defalut: './out')")
parser.add_argument("--plot", type=bool, default=True, help=f"To save the figure, set `--plot=True`. (defalut: True)")
args = parser.parse_args()

@lru_cache
def minus_fibonacci(n : int) -> Union[Callable, int]:
    """
    Fibonacci function for domain with negative values.
    :param n: A number with negative integer.
    :type n: int
    :return: n-th Fibonacci value in negative direction.
    :rtype: Union[Callable, int]
    """
    if n > 0:
        raise ValueError(f"The number should be negative. (Error value: {n = })")
    return 0 if n == 0 else -1 if n == -1 else minus_fibonacci(n+2) - minus_fibonacci(n+1)

@lru_cache
def plus_fibonacci(n : int) -> Union[Callable, int]:
    """
    Fibonacci function for domain with positive values.
    :param n: A number with positive integer.
    :type n: int
    :return: n-th Fibonacci value in positive direction.
    :rtype: Union[Callable, int]
    """
    if n < 0:
        raise ValueError(f"The number should be positive. (Error value: {n = })")
    return 0 if n == 0 else 1 if n == 1 else plus_fibonacci(n-1) + plus_fibonacci(n-2)

def draw_graph(x_min : int, x_max : int) -> None:
    x = [i for i in range(x_min, x_max+1)]
    y = [minus_fibonacci(n) if n < 0 else plus_fibonacci(n) if n > 0 else 0 for n in x]
    # Plot
    plt.plot(x, y, label="Fibonacci")
    plt.xlabel("Number")
    plt.ylabel("Fibonacci Value")
    plt.title("Fibonacci Sequence")
    plt.legend()
    plt.grid(True)
    if args.plot: 
        plt.savefig(f"{args.dir}/x_range{x_min, x_max}")
    plt.show()

def main() -> None:
    draw_graph(args.min, args.max)

# Main
if __name__ == "__main__":
    main()