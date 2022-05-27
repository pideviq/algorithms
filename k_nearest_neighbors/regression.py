"""Smart Bakery problem.

Suppose you run a small bakery in Berkeley,
and you make fresh bread every day. You’re trying to predict how many
loaves to make for today. You have a set of features:
• Weather on a scale of 1 to 5 (1 = bad, 5 = great).
• Weekend or holiday? (1 if it’s a weekend or a holiday, 0 otherwise.)
• Is there a game on? (1 if yes, 0 if no.)

Based on the given historical data current conditions, how many loaves will
you sell?
"""


from __future__ import annotations
from typing import List, Tuple, Dict
from math import sqrt, ceil
from statistics import fmean


# Conditions for today:
#   weather (from 1 to 5),
#   is it a weekend (1 or 0),
#   is there a game on (1 or 0)
Conditions = Tuple[int, int, int]
# Day result: (Conditions, number of sold loaves)
DayResult = Tuple[Conditions, int]


def calc_pythagorean_distance(point_a: Conditions, point_b: Conditions,
                              boost: bool = False) -> int | float:
    """Return a distance between two points counted by Pythagorean formula."""
    total = sum((x-y) ** 2 for x, y in zip(point_a, point_b))
    return total if boost else round(sqrt(total), 4)


class SmartBakery:
    """A bakery, that uses KNN algorithm to predict sales."""

    # Historical data of conditions and sold loaves of bread
    sales_report: List[DayResult]
    # Number of nearest neighbors for calculations
    k: int

    def __init__(self, sales_report, k: int = None):
        self.sales_report = sales_report
        self.k = ceil(sqrt(len(sales_report))) if k is None else k

    def make_sales_forecast(self, conditions: Conditions,
                            boost: bool = False) -> int:
        """Return optimal amount of loaves to make today."""
        try:
            distances = {
                key: calc_pythagorean_distance(day[0], conditions, boost=boost)
                for key, day in enumerate(self.sales_report)
            }
        except (ValueError, IndexError, TypeError):
            raise ValueError('wrong format of sales_report')

        closest_days = self._get_closest_days(distances)
        sales = [self.sales_report[key][1] for key in closest_days]
        return ceil(fmean(sales))

    def _get_closest_days(self, distances) -> Dict[int, int]:
        """Return k days with the closest conditions."""
        keys = sorted(distances, key=distances.get)[:self.k]
        return {key: distances[key] for key in keys}
