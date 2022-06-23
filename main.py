from bytewax import Dataflow, run


flow = Dataflow()
flow.map(lambda x: x * x)
flow.capture()


if __name__ == "__main__":
    for epoch, x in sorted(run(flow, enumerate(range(10)))):
        print(x)