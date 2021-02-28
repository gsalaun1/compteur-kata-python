import unittest
from CounterImpl import CounterImpl


class CounterImplTest(unittest.TestCase):
    counterimpl: CounterImpl

    def setUp(self) -> None:
        self.counterimpl = CounterImpl()
        super().setUp()

    def test_should_init_counter_with_one_wheel_having_0_as_max_value(self):
        self.counterimpl.init([0])
        self.assertEqual(self.counterimpl.current(), [0])

    def test_should_not_increment_counter_if_it_has_one_wheel_having_0_as_max_value(self):
        self.counterimpl.init([0])
        self.counterimpl.next()
        self.assertEqual(self.counterimpl.current(), [0])

    def test_should_not_have_next_value_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counterimpl.init([0])
        self.assertFalse(self.counterimpl.hasnext())

    def test_should_have_one_possible_value_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counterimpl.init([0])
        self.assertEquals(self.counterimpl.nbpossiblevalues(), 1)

    def test_should_have_no_remaining_values_if_counter_has_one_wheel_having_0_as_max_value(self):
        self.counterimpl.init([0])
        self.assertEquals(self.counterimpl.nbremainingvalues(), 0)
