from src.business_logic import add_two


def test_add_two():
    test_input = {"number": 5}
    assert add_two(test_input) == 7


# Try commenting this test out and
# re-run `make run-all-tests`
def test_add_two_bad_input():
    bad_input_1 = {"not_number": 12}
    bad_input_2 = {"something_else_entirely": False}
    bad_input_3 = {"number": "sandwich"}

    assert add_two(bad_input_1) == None
    assert add_two(bad_input_2) == None
    assert add_two(bad_input_3) == None
