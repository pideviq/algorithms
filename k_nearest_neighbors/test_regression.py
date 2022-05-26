import unittest
from math import sqrt, ceil
from k_nearest_neighbors.regression import SmartBakery


class TestRegression(unittest.TestCase):
    """Test regression."""

    def setUp(self) -> None:
        self.sales_report = [
            ((5, 1, 0), 300),
            ((3, 1, 1), 225),
            ((1, 1, 0), 75),
            ((4, 0, 1), 200),
            ((4, 0, 0), 150),
            ((2, 0, 0), 50),
        ]
        self.k = ceil(sqrt(len(self.sales_report)))
        self.conditions = (4, 1, 0)
        self.loaves_to_make = 219

    def test_default_smart_bakery_init(self) -> None:
        """Test initialization of default bakery."""
        default_bakery = SmartBakery(self.sales_report)
        self.assertEqual(self.sales_report, default_bakery.sales_report)
        self.assertEqual(self.k, default_bakery.k)

    def test_custom_smart_bakery_init(self) -> None:
        """Test initialization of bakery with custom k."""
        careless_k = 1
        careless_bakery = SmartBakery(self.sales_report, careless_k)
        self.assertEqual(self.sales_report, careless_bakery.sales_report)
        self.assertEqual(careless_k, careless_bakery.k)

    def test_forecast(self) -> None:
        """Test forecast algorithm."""
        bakery = SmartBakery(self.sales_report, 4)
        loaves_to_make = bakery.make_sales_forecast(self.conditions)
        self.assertEqual(self.loaves_to_make, loaves_to_make)

    def test_forecast_for_exact_match(self) -> None:
        """Test forecast for the same conditions and k=1."""
        conditions = (4, 0, 1)
        bakery = SmartBakery(self.sales_report, 1)
        loaves_to_make = bakery.make_sales_forecast(conditions)
        self.assertEqual(200, loaves_to_make)

    def test_incorrect_report(self) -> None:
        """Test handling of a report with wrong format."""
        bad_report = [
            (300, (5, 1, 0)),
            (225, (3, 1, 1)),
        ]
        bakery = SmartBakery(bad_report)
        with self.assertRaises(ValueError):
            bakery.make_sales_forecast((5, 1, 0))


if __name__ == '__main__':
    unittest.main()
