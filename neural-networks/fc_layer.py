from layer import Layer
import numpy as np

class FCLayer(Layer):
    # input_size: number of input neurons
    # output_size: number of output neurons
    def __init__(self, input_size, output_size) -> None:
        super().__init__()
        self.weights = np.random.rand(input_size, output_size) * 0.01
        self.bias = np.zeros(shape=(1, output_size))