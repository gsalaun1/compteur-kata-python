import unittest

from CounterImpl import CounterImpl


class TwoWheelsCounterImplTest(unittest.TestCase):
    counter: CounterImpl

    def setUp(self) -> None:
        self.counter = CounterImpl()

    def test_should_init_counter_with_two_wheels_having_0_as_max_value(self):
        self.counter.init([0, 0])
        self.assertEqual([0, 0], self.counter.current())
