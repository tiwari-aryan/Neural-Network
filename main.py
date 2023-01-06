class Neuron:
    def __init__(self, inputs, weights, bias):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias
        self.val = self.compute()

    def compute(self):
        neuron_val = 0
        for neuron_input, neuron_weights in zip(self.inputs, self.weights):
            neuron_val += neuron_input * neuron_weights
        return neuron_val + self.bias


class Layer:
    def __init__(self, inputs, weights, biases):
        self.inputs = inputs
        self.weights = weights
        self.biases = biases
        self.neurons = self.compute()
        self.size = len(self.neurons)

    def compute(self):
        layer_neurons = []
        for weights, bias in zip(self.weights, self.biases):
            neuron = Neuron(self.inputs, weights, bias)
            layer_neurons.append(neuron)
        return layer_neurons

    def print_layer(self):
        for neuron in self.neurons:
            print(neuron.val)


inputs = [1.1, 2.7, 9.2, 2]
weights = [
    [1.5, 2.1, 0.2, 1.5],
    [2, 1, 3.4, 7.1],
    [8.2, 3.1, 2.2, 1.5],
]
biases = [2, 3, 1.2]

layer = Layer(inputs, weights, biases)

layer.print_layer()
