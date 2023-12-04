import random
import pytest
# from pytest import nonempty_list_of
from SemGus_bit_vector import synthesize_program

# Example usage
specification = "flipBit(x), x == [0, 1, 0] -> [1, 0, 1]"
testCases = [
    ([0, 1, 0], [1, 0, 1]),
    ([0, 1, 0, 1, 0], [1, 0, 1, 0, 1]),
    ([1, 0, 1, 0, 1], [0, 1, 0, 1, 0]),
    ([0, 0, 0, 0], [1, 1, 1, 1]),
    ([1, 1, 1, 1], [0, 0, 0, 0]),
    ([0], [1]),
    ([1], [0]),
    ([0] * 20, [1] * 20),
    ([1] * 20, [0] * 20),
    ([1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1]),
    ([0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0]),
    ([], [])
    # ... any additional test cases you wish to add
]


def test_synthesize_program():
    (result_program, result_program_code), score = synthesize_program(specification, testCases)
    print("Result Program Code:", result_program_code)
    print("Result from Program:", result_program([0, 1, 0]))
    assert score == len(testCases)

#def test_spec1()
#def test_spec2()


test_synthesize_program()


# -------- Tests with PyTest QuickCheck

# @pytest.mark.randomize(l=nonempty_list_of(int))
# def test_synthesize_program(specification, l):
#     pass











#testing with quickcheck randomize fn
#@pytest.mark.randomize(list(i1=int, i2=int, ncalls=5))
#THEIR CODE AS TEMPLATE: def test_generate_ints(i1, i2):
#def result_program(i1, i2):
#    pass

#@pytest.mark.randomize(min_num=0, max_num=2, ncalls=5)
#def test_generate_int_anns(i1: int):
#    pass



