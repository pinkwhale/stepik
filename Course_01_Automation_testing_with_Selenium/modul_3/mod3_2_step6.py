
assert abs(-42) == 42, "Should be absolute value of a number"


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

print(test_input_text(8, 11))

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

def test_substring1(full_string, substring):
    assert full_string.find(substring) != -1, f"expected '{substring}' to be substring of '{full_string}'"