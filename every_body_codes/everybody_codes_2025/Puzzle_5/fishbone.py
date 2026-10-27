from pip._internal.resolution.resolvelib import provider


class SpinePiece:
    def __init__(self, id):
        self.spine = id
        self.left = None
        self.right = None
        self.parent = None
        self.child = None
        self.level = 0

    @property
    def level_value(self):
        left = str(self.left) if self.left is not None else ""
        right = str(self.right) if self.right is not None else ""
        value = left + str(self.spine) + right
        return int(value)

    def print_SpinePiece(self):
        print(f"{self.left if self.left is not None else "_"}\t"
              f"{self.spine}\t"
              f"{self.right if self.right is not None else "_"}")


class Fishbone:
    def __init__(self, simplified_structure: str):
        id, sequence = simplified_structure.split(":")
        self.sword_id: int = int(id)
        self.sequence: list[int] = [int(each) for each in sequence.split(",")]
        self.head: SpinePiece = SpinePiece(self.sequence.pop(0))
        self.head.level = 1
        self.quality: str = str(self.head.spine)
        self._build_fishbone()

    def _build_fishbone(self):
        while len(self.sequence) > 0:
            new_value = self.sequence.pop(0)
            current = self.head
            while current is not None:
                if new_value < current.spine and current.left is None:
                    # Set Left
                    current.left = new_value
                    break
                elif new_value > current.spine and current.right is None:
                    # set right
                    current.right = new_value
                    break
                elif current.child is None:
                    # Make A new child and Exit
                    new_spine = SpinePiece(new_value)
                    self.quality = self.quality + str(new_value)
                    current.child = new_spine
                    new_spine.parent = current
                    new_spine.level = current.level + 1
                    break
                else:
                    # Move to next
                    current = current.child

    def get_quality(self):
        return int(self.quality)

    def get_level_values(self):
        current = self.head
        value = {}
        while current is not None:
            value[current.level] = current.level_value
            current = current.child
        return value


    def print_Fishbone(self):
        current = self.head
        while current is not None:
            current.print_SpinePiece()
            current = current.child
