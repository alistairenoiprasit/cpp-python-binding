#
# Created by Alistaire Noiprasit on 11/11/2025.
#

from pathlib import Path

from tqdm import tqdm

from calc_binding_alistaire_noiprasit import Calculator

print(Calculator().add(1, 2))

class FileCalculator(Calculator):
    def sum_file(self, path=None):
        if path is None:
            path = Path(__file__).parent / "nums.csv"

        with tqdm(total=100_100_100, desc="Summing numbers from file") as pbar:
            total = 0
            with open(path, 'r') as file:
                for line in tqdm(file, desc="Summing numbers from file"):
                    number = float(line.strip())
                    total = self.add(total, number)
            return total