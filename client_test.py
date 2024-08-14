import unittest
from client3 import getDataPoint, getRatio  # Import the methods to be tested


class ClientTest(unittest.TestCase):
    # Test getDataPoint for normal cases where ask price is not always greater than bid price
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate over the list of quotes and test each one
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(
                quote)  # Call getDataPoint
            expected_price = (bid_price + ask_price) / \
                2  # Calculate the expected price

            # Assert that the returned tuple matches the expected output
            self.assertEqual((stock, bid_price, ask_price, price), (
                quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))

    # Test getDataPoint when the bid price is greater than the ask price
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate over the list of quotes and test each one
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(
                quote)  # Call getDataPoint
            expected_price = (bid_price + ask_price) / \
                2  # Calculate the expected price

            # Assert that the returned tuple matches the expected output
            self.assertEqual((stock, bid_price, ask_price, price), (
                quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))

    # Test getRatio when both prices are valid and non-zero
    def test_getRatio_validInput(self):
        price_a = 120.0
        price_b = 60.0
        # Assert that getRatio returns the correct ratio
        self.assertEqual(getRatio(price_a, price_b), 2.0)

    # Test getRatio when the second price (price_b) is zero
    def test_getRatio_zeroPriceB(self):
        price_a = 120.0
        price_b = 0.0
        # Assert that getRatio returns None to avoid division by zero
        self.assertIsNone(getRatio(price_a, price_b))

    # Test getRatio when the first price (price_a) is zero
    def test_getRatio_zeroPriceA(self):
        price_a = 0.0
        price_b = 120.0
        # Assert that getRatio correctly returns 0.0
        self.assertEqual(getRatio(price_a, price_b), 0.0)


if __name__ == '__main__':
    unittest.main()
