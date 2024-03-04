# Who Created Me
![banner](./assets/banner.webp)

## What is this?

This is a tool to automatically track which piece of code created your data.

In particular, every time you save a numpy array or a torch tensor, this tool
will automatically create a file with metadata about the code that created the data.

```bash
.
├── data.npy
└── .data.npy.who
```

```bash
cat .data.npy.who
───────┬─────────────────────────────────────────────────────────────────────
       │ File: .data.npy.who
───────┼─────────────────────────────────────────────────────────────────────
   1   │ Script Path: /path/to/example_numpy.py
   2   │ -------------------------------------------------------
   3   │ Code:
   4   │ -------------------------------------------------------
   5   │ import numpy as np
   6   │ import whocreatedme as wcme
   7   │ wcme.trace(numpy=True)
   8   │
   9   │ np.save("./test.npy", np.random.randn(50, 50))
  10   │ -------------------------------------------------------
───────┴─────────────────────────────────────────────────────────────────────

```



## How to use

You can either use the CLI or the Python API:

### CLI

```bash
python -m whocreatedme.cli <your-script> [--npsave] [--torchsave]
```

For example, to trace both `numpy` and `torch` `save` methods
for a script `script.py`, simply run:

```bash
python -m whocreatedme.cli script.py --npsave --torchsave
```

### Python API
Alternatively, you can trace the `numpy` and `torch` `save` methods
from your code by using the Python API:

```python
import numpy as np
import whocreatedme
whocreatedme.trace()

# this will automatically create a file `.data.npy.who` in the same directory as `data.npy`
np.save("data.npy", np.array([1, 2, 3]))
```

## Install

```bash
pip install whocreatedme
```

## Limitations

For now, this lightweight module only supports monkey-patching the `.save()`
methods in `numpy` and `torch`.

---
Images in README created with DALL-E.
