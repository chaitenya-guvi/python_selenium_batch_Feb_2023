import pytest


# file name should be starting with test_
# function name should start with test_

# Different ways of running
# 1. pytest filename
# 2. pytest -s -v filename      more verbose output
# 3. pytest -s -v filename::function     run specific function inside the test
# 4. pytest -q test_selenium8_pytestt_example.py --html=filename.html     run specific function inside the test


# @pytest.fixture()
# def setUp():
#     print("Running demo2 setUp")
#     yield
#     print("Running demo2 tearDown")

def test_demo_methodA():
    print("\n **********Running demo2 method A***********")


def test_demo_methodB():
    print("\n **********Running demo2 method B***********")