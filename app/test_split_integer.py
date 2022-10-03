from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(49, 3)) == 49
    assert sum(split_integer(56, 6)) == 56
    assert sum(split_integer(211, 6)) == 211


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(9, 3) == [3, 3, 3]
    assert split_integer(27, 3) == [9, 9, 9]
    assert split_integer(256, 4) == [64, 64, 64, 64]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(16, 1) == [16]
    assert split_integer(15, 1) == [15]
    assert split_integer(13, 1) == [13]
    assert split_integer(28413, 1) == [28413]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]
    assert split_integer(3, 4) == [0, 1, 1, 1]
