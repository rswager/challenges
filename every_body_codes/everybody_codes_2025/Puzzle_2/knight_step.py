from typing import Self

class KnightStep:
    def __init__(self,A):
        self.value: list[int] = A

    def __add__(self, right_value: KnightStep | list[int]) -> Self:
        if isinstance(right_value, KnightStep):
            right_value = right_value.value
        return self.add_values(left_value=self.value, right_value=right_value)

    def __radd__(self, left_value: KnightStep | list[int]) -> Self:
        if isinstance(left_value, KnightStep):
            left_value = left_value.value
        return self.add_values(left_value = left_value, right_value = self.value)

    def add_values(self, left_value: list[int], right_value: list[int]) -> Self:
        #print(f"{left_value} + {right_value} = ", end="")
        return self.__class__([
            left_value[0] + right_value[0], # X1 + X2
            left_value[1] + right_value[1]  # Y1 + Y2
        ])

    def __mul__(self, right_value: KnightStep | list[int]) -> Self:
        if isinstance(right_value, KnightStep):
            right_value = right_value.value
        return self.mul_values(left_value=self.value, right_value=right_value)

    def __rmul__(self, left_value: KnightStep | list[int]) -> Self:
        if isinstance(left_value, KnightStep):
            left_value = left_value.value
        return self.mul_values(left_value=left_value, right_value=self.value)

    def mul_values(self, left_value: list[int], right_value: list[int]) -> Self:
        #print(f"{left_value} * {right_value} = ", end="")
        return self.__class__([
            left_value[0] * right_value[0] - left_value[1] * right_value[1], # X1 * X2 - Y1 * Y2
            left_value[0] * right_value[1] + left_value[1] * right_value[0]  # X1 * Y2 + Y1 * X2

        ])

    def __truediv__(self, right_value: KnightStep | list[int]) -> Self:
        if isinstance(right_value, KnightStep):
            right_value = right_value.value
        return self.truediv_values(left_value=self.value, right_value=right_value)

    def __rtruediv__(self, left_value: KnightStep | list[int]):
        if isinstance(left_value, KnightStep):
            left_value = left_value.value
        return self.truediv_values(left_value=left_value, right_value=self.value)

    def truediv_values(self, left_value: list[int], right_value: list[int]) -> Self:
        #print(f"{left_value} / {right_value} = ", end="")
        return self.__class__([
            int(int(left_value[0]) / int(right_value[0])),  # X1 / X2
            int(int(left_value[1]) / int(right_value[1])),  # Y1 / Y2
        ])
    def __str__(self):
        return str(self.value)