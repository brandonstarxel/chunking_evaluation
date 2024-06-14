from typing import Callable

class GeneralBenchmark:
    def __init__(self, name: str, description: str, benchmark: Callable):
        self.name = name
        self.description = description
        self.benchmark = benchmark

    def run(self):
        self.benchmark()