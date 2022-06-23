from bytewax import Dataflow, run

def test_run():
    # arrange
    flow = Dataflow()
    flow.filter(is_odd_number)
    flow.capture()
    input = [(0, 11), (0, 73), (0, 50)]

    # act
    result = run(flow, input)

    # assert
    assert sorted(result) == sorted([(0, 11), (0, 73)])

def is_odd_number(x):
    return x % 2 == 1