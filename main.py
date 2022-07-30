from bytewax import Dataflow, run

def is_odd_number(x):
   return x % 2 == 1

#Bytewax dataflow
flow = Dataflow()
flow.filter(is_odd_number)
flow.capture()

def test_run1():
   #arrange
   inputData = [(0, 11), (0, 73), (0, 50)]
   #act by running the bytewax flow
   result = run(flow, inputData)
   # assert
   assert sorted(result) == sorted([(0, 11), (0, 73)])

def test_run2():
   #arrange
   inputData = [(0, 1), (0, 3), (0, 50)]
   #act by running the bytewax flow
   result = run(flow, inputData)
   # assert
   assert sorted(result) == sorted([(0, 1), (0, 3)])

def test_run3():
   #arrange
   inputData = [(0, 12), (0, 72), (0, 5)]
   #act by running the bytewax flow
   result = run(flow, inputData)
   # assert
   assert sorted(result) == sorted([(0, 5)])
