import unittest
from ring_buffer import RingBuffer


class TestRingBuffer(unittest.TestCase):
    def test_init_raises_when_called_with_negative_size(self):
        with self.assertRaises(ValueError):
            RingBuffer(-1)

    def test_write_return_items_inserted(self):
        instance = RingBuffer(5)
        actual = instance.write([1, 2, 3, 4, 5])
        self.assertEqual(actual, 5)

    def test_write_return_actual_items_inserted_when_it_filled_up(self):
        instance = RingBuffer(3)
        actual = instance.write([1, 2, 3, 4, 5])
        self.assertEqual(actual, 3)

    def test_read_raises_when_called_on_empty_buffer(self):
        instance = RingBuffer(5)
        with self.assertRaises(IndexError):
            instance.read()

    def test_read_return_first_element(self):
        instance = RingBuffer(5)
        instance.write([1, 2, 3, 4, 5])
        actual = instance.read()
        self.assertEqual(actual, 1)

    def test_read_works_after_several_writes(self):
        instance = RingBuffer(3)
        self.assertEqual(instance.write([1, 2]), 2)
        self.assertEqual(instance.read(), 1)
        self.assertEqual(instance.write([3, 4]), 2)
        self.assertEqual(instance.read(), 2)
        self.assertEqual(instance.write([5, 6]), 1)
        self.assertEqual(instance.read(), 3)

    def test_acceptance(self):
        instance = RingBuffer(5)
        self.assertEqual(instance.write([1, 2, 3]), 3)
        self.assertEqual(instance.write([4, 5, 6]), 2)
        self.assertEqual(instance.read(), 1)
        self.assertEqual(instance.read(), 2)
        self.assertEqual(instance.read(), 3)


if __name__ == '__main__':
    unittest.main()