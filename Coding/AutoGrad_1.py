# Create Tensors:

x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)

# Build a Computational Graph:

y = w * x + b

# Compute Gradients.

y.backward()

# Printing the gradients:

print(x.grad)
print(w.grad)
print(b.grad)