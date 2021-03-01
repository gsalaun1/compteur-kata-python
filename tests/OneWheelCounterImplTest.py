import unittest

from CounterImpl import CounterImpl


class OneWheelCounterImplTest(unittest.TestCase):
    counter: CounterImpl

    def setUp(self) -> None:
        self.counter = CounterImpl()

    def test_should_init_counter_with_one_wheel_having_0_as_max_value(self):
        self.counter.init([0])
        self.assertEqual([0], self.counter.current())

    def test_should_not_increment_counter_if_it_has_one_wheel_having_0_as_max_value(self):
        self.counter.init([0])
        self.counter.next()
        self.assertEqual([0], self.counter.current())

    def test_should_not_have_next_value_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counter.init([0])
        self.assertFalse(self.counter.hasnext())

    def test_should_have_one_possible_value_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counter.init([0])
        self.assertEqual(1, self.counter.nbpossiblevalues())

    def test_should_have_no_remaining_values_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counter.init([0])
        self.assertEqual(0, self.counter.nbremainingvalues())

    def test_should_init_counter_with_one_wheel_having_1_as_max_value(self):
        self.counter.init([1])
        self.assertEqual([0], self.counter.current())

    def test_should_increment_counter_if_it_has_one_wheel_having_1_as_max_value(self):
        self.counter.init([1])
        self.counter.next()
        self.assertEqual([1], self.counter.current())

    def test_should_not_increment_counter_if_it_has_one_wheel_having_1_as_max_value_and_max_value_reached(self):
        self.counter.init([1])
        for i in range(2):
            self.counter.next()

        self.assertEqual([1], self.counter.current())

    def test_should_have_next_value_if_counter_has_one_wheel_having_1_as_max_value(self):
        self.counter.init([1])
        self.assertTrue(self.counter.hasnext())

    def test_should_not_have_next_value_if_counter_has_one_wheel_having_1_as_max_value_and_max_value_reached(self):
        self.counter.init([1])
        self.counter.next()
        self.assertFalse(self.counter.hasnext())

    def test_should_have_two_possible_values_if_counter_has_one_wheel_having_1_as_max_value(self):
        self.counter.init([1])
        self.assertEqual(2, self.counter.nbpossiblevalues())

    def test_should_have_one_remaining_value_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counter.init([1])
        self.assertEqual(1, self.counter.nbremainingvalues())

    def test_should_have_no_remaining_value_if_counter_has_one_wheel_having_0_as_max_value_and_max_value_reached(self):
        self.counter.init([1])
        self.counter.next()
        self.assertEqual(0, self.counter.nbremainingvalues())
