import unittest

from CounterImpl import CounterImpl


class TwoWheelsCounterImplTest(unittest.TestCase):
    counter: CounterImpl

    def setUp(self) -> None:
        self.counter = CounterImpl()

    def test_should_init_counter_with_two_wheels_having_0_as_max_value(self):
        self.counter.init([0, 0])
        self.assertEqual([0, 0], self.counter.current())

    def test_should_not_increment_counter_if_it_has_two_wheels_having_0_as_max_value(self):
        self.counter.init([0, 0])
        self.counter.next()
        self.assertEqual([0, 0], self.counter.current())

    def test_should_not_increment_counter_if_it_has_two_wheels(self):
        self.counter.init([0, 1])
        self.counter.next()
        self.assertEqual([0, 1], self.counter.current())

    def test_should_not_have_next_value_if_counter_has_two_wheels_having_0_as_max_value(self):
        self.counter.init([0, 0])
        self.assertFalse(self.counter.hasnext())

    def test_should_not_have_next_value_if_counter_has_two_wheels_and_all_reached_max_values(self):
        self.counter.init([0, 1])
        self.counter.next()
        self.assertFalse(self.counter.hasnext())

    def test_should_have_next_value_if_counter_has_two_wheels(self):
        self.counter.init([0, 1])
        self.assertTrue(self.counter.hasnext())
