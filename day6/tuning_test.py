import unittest
import tuning

class TuningTests(unittest.TestCase):

    def test_has_unique_chars_true(self):
        result = tuning.has_unique_chars("abcd")
        self.assertTrue(result)

    def test_has_unique_chars_false(self):
        result = tuning.has_unique_chars("ccdb")
        self.assertFalse(result)

    def test_get_start_of_packet_marker(self):
        input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        result = tuning.get_start_of_packet_marker(input, 4)
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()