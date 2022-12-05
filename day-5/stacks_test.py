import pathlib
import unittest
import stacks

TESTDATA_FILENAME = pathlib.Path(__file__).parent.joinpath("input_test.txt")

class TestStacks(unittest.TestCase):

    def setUp(self):
        self.testdata = open(TESTDATA_FILENAME).read()

    def test_clean_input_data(self):
        result = stacks.clean_input_data(self.testdata)

        expected = [[
            "    [D]    ", 
            "[N] [C]    ", 
            "[Z] [M] [P]", 
            ],
            [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
            ]]

        self.assertEqual(result, expected)
    
    def test_find_indices(self):
        graph_line = "[Z] [M] [P]"

        result = stacks.find_indices(graph_line, '[')

        self.assertEqual(result, [0, 4, 8])

    def test_get_stacks(self):
        graph = [
            "    [D]    ", 
            "[N] [C]    ", 
            "[Z] [M] [P]", 
            ]
        
        result = stacks.get_stacks(graph)

        expected = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

        self.assertEqual(result, expected)

    def test_move_crates_single(self):

        all_stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

        result = stacks.move_crates(all_stacks, 1, 2, 1)

        expected = [['Z', 'N', 'D'], ['M', 'C'], ['P']]

        self.assertEqual(result, expected)

    def test_move_crates_multiple(self):

        all_stacks = [['Z', 'N', 'D'], ['M', 'C'], ['P']]

        result = stacks.move_crates(all_stacks, 3, 1, 3)

        expected = [[], ['M', 'C'], ['P', 'D', 'N', 'Z']]

        self.assertEqual(result, expected)

    def test_get_top_crate(self):

        all_stacks = [['Z', 'N', 'D'], ['M', 'C'], ['P']]

        result = stacks.get_top_crates(all_stacks)

        self.assertEqual(result, 'DCP')

    def test_read_procedure(self):

        procedure_line = "move 1 from 2 to 1"

        result = stacks.read_procedure(procedure_line)

        self.assertEqual(result, {'count': 1, 'last_pos': 2, 'new_pos': 1})

if __name__ == "__main__":
    unittest.main()