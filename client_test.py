import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        # Test the getDataPoint function with regular bid and ask prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, bid_price)  # Check if the price is correctly set as the bid price

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        # Test the scenario where the bid price is greater than the ask price
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            if bid_price > ask_price:
                self.assertTrue(bid_price > ask_price)  # Validate that the bid price is indeed greater than the ask price

    def test_getDataPoint_sameBidAsk(self):
        quote = {'top_ask': {'price': 120.5, 'size': 50}, 'timestamp': '2020-01-01 12:00:00.000000', 'top_bid': {'price': 120.5, 'size': 50}, 'stock': 'GHI'}
        # Test the case where the bid and ask prices are the same
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(bid_price, ask_price)  # Assert that bid and ask prices are the same

# Additional unit tests can be added here to test different scenarios

if __name__ == '__main__':
    unittest.main()

