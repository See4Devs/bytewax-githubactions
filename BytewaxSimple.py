from bytewax import Dataflow, run

def is_odd_number(x):
   return x % 2 == 1

#Bytewax dataflow
flow = Dataflow()
flow.filter(is_odd_number)
flow.capture()

inputData = [(0, 11), (0, 73), (0, 50)]

if __name__ == "__main__":
    for epoch, x in sorted(run(flow,inputData)):
        print(x)
