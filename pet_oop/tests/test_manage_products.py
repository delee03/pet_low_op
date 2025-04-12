import unittest

from models.owner import Owner
from models.Manage import ManageProducts

class TestManageProducts(unittest.TestCase):
    def setUp(self):
        # Khởi tạo Owner và ManageProducts trước mỗi test case
        self.owner = Owner("Alice", "0123", "Hà Nội")
        self.product = ManageProducts("Laptop", 1000.0, "Electronics")

    def test_get_info(self):
        # Test phương thức get_info()
        expected_info = "Product: Laptop, Price: 1000.0, Category: Electronics"
        self.assertEqual(self.product.get_info(), expected_info)

    def test_apply_product(self):
        # Test phương thức apply_product() với giảm giá 10%
        discounted_price = self.product.apply_product(10.0)
        self.assertEqual(discounted_price, 900.0)

    def test_apply_product_with_zero_discount(self):
        # Test trường hợp không giảm giá (giảm giá 0%)
        discounted_price = self.product.apply_product(0.0)
        self.assertEqual(discounted_price, 1000.0)

if __name__ == '__main__':
    unittest.main()
