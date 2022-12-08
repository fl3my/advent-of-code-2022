import unittest
import pathlib
import device

TEST_FILE = pathlib.Path(__file__).parent.joinpath("input_test.txt")


class DeviceTests(unittest.TestCase):

    def test_sum_of_directories(self):
        lines = device.get_stripped_lines('input_test.txt')
        directory = device.convert_to_dir_dict(lines)
        result = device.sum_of_directories(directory, 100000)
        self.assertEqual(result, 95437)


if __name__ == "__main__":
    unittest.main()
