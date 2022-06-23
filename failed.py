#sample work that throws an error
from bytewax import Dataflow, run

flow = Dataflow()
flow.map(lambda x: test_function(x))
flow.capture()


def test_function(y):
   x = 10;
   z = 5;
   for index in range(y):
       print(index * x)
       x += 1
   del (x)

   print("Final value of x:")
   print(x)
   del (x)


if __name__ == "__main__":
   for x in sorted(run(flow, enumerate(range(10)))):
       print(x)
