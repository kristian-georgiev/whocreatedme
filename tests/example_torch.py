import torch
import whocreatedme as wcme

wcme.trace(torch=True)

torch.save(torch.randn(50, 50), "./test.pt")
