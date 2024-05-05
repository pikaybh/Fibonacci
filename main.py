import matplotlib.pyplot as plt
from functools import lru_cache
from typing import (Callable, Union)


@lru_cache
def minus_fibonacci(n : int) -> Union[Callable, int]:
    if n > 0:
        raise ValueError(f"The number should be negative. (Error value: {n = })")
    return 0 if n == 0 else -1 if n == -1 else minus_fibonacci(n+2) - minus_fibonacci(n+1)

@lru_cache
def plus_fibonacci(n : int) -> Union[Callable, int]:
    if n < 0:
        raise ValueError(f"The number should be positive. (Error value: {n = })")
    return 0 if n == 0 else 1 if n == 1 else plus_fibonacci(n-1) + plus_fibonacci(n-2)

def draw_graph(x_min : int, x_max : int) -> None:
    # x축 범위 설정
    x_range = [i for i in range(x_min, x_max+1)]
    # 각각의 Fibonacci 함수에 대해 y값 계산
    minus_fibonacci_values = [minus_fibonacci(n) for n in filter(lambda x: x < 0, x_range)]
    plus_fibonacci_values = [plus_fibonacci(n) for n in filter(lambda x: x >= 0, x_range)]
    y_range = minus_fibonacci_values + plus_fibonacci_values

    # 그래프 그리기
    plt.plot(x_range, y_range, label="Fibonacci")
    plt.xlabel("Number")
    plt.ylabel("Fibonacci Value")
    plt.title("Fibonacci Sequence")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./out/x_range{x_min, x_max}")
    plt.show()

def main() -> None:
    draw_graph(-50, 50)

# Main
if __name__ == "__main__":
    main()