# JSONx Python

A Python implementation of [JSONx](https://github.com/getformative/jsonx).

## Installation

```bash
pip install jsonx-py
```

## Unflattening JSON

```python
import jsonx

data = {
  "user.name": "Anakin Skywalker",
  "user.email": "anakin@jedi.galaxy",
}

jsonx.unflatten(data)
```
