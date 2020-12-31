
from auto.conftest import create_task_help

# from auto.plan.ApiTest.test_cachedemo import test_a
# def test_b(test_a):

#     a = test_a
#     print(a)

# def test_c(test_a):

#     a = test_a
#     print(a)

def test_d(create_task_help):
    a, b = create_task_help
    print(a)