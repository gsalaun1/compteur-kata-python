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

    def test_should_not_increment_counter_if_it_has_two_wheels_and_max_value_reached(self):
        self.counter.init([0, 1])
        self.counter.next()
        self.assertEqual([0, 1], self.counter.current())

    def test_should_increment_counter_if_it_has_two_wheels_right_wheel_at_max_left_wheel_not_at_max(self):
        self.counter.init([1, 1])
        self.counter.next()
        self.counter.next()
        self.assertEqual([1, 0], self.counter.current())

    def test_should_not_have_next_value_if_counter_has_two_wheels_and_all_reached_max_values(self):
        self.counter.init([0, 1])
        self.counter.next()
        self.assertFalse(self.counter.hasnext())

    def test_should_have_next_value_if_counter_has_two_wheels(self):
        self.counter.init([0, 1])
        self.assertTrue(self.counter.hasnext())

    def test_should_have_next_value_if_counter_has_two_wheels_having_not_0_as_max_value(self):
        self.counter.init([2, 2])
        for _ in range(4):
            self.counter.next()
        self.assertTrue(self.counter.hasnext())

    def test_should_count_possible_values_if_counter_has_two_wheels_having_0_as_max_value(self):
        self.counter.init([0, 0])
        self.assertEqual(1, self.counter.nbpossiblevalues())

    def test_should_count_possible_values_if_counter_has_two_wheels_having_1_as_max_value(self):
        self.counter.init([1, 1])
        self.assertEqual(4, self.counter.nbpossiblevalues())

    def test_should_count_remaining_values_at_start_if_counter_has_two_wheels_having_1_as_max_value(self):
        self.counter.init([1, 1])
        self.assertEqual(3, self.counter.nbremainingvalues())

    def test_should_count_remaining_values_after_increment_if_counter_has_two_wheels_having_1_as_max_value(self):
        self.counter.init([1, 1])
        self.counter.next()
        self.assertEqual(2, self.counter.nbremainingvalues())

    def test_should_count_remaining_values_after_two_increments_if_counter_has_two_wheels_having_1_as_max_value(self):
        self.counter.init([1, 1])
        for _ in range(2):
            self.counter.next()
        self.assertEqual(1, self.counter.nbremainingvalues())
