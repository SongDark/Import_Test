# How to import from father/cousin/nephew path?

# Question Description
In `./pipelines/_train.py`, aim to import something from 3 different path levels:

1. `./_config.py` (in father path)
2. `./networks/_cnn.py` (in cousin path)
3. `./networks/autoencoder/encoder.py` (in nephew path)

# Solution

## Step one: write __init__.py

1. Add `__init__.py` in each path where there exits more than one files, such as `./networks/__init__.py`.
2. Import everything necessary under the same path, for example, import `encoder` and `decoder` in `./networks/autoencoder/__init__/py`.

## Step two: add path in the file you wanna run

In Python 3.6.7, it's unfeasible to use the script below in `_train.py` to import files under `./networks`:

```python
    import sys
    sys.path.append("..")
```

because the current path you run `_train.py` is `./pipelines/`, you have to add this scipt in `_train.py`:

```python
    sys.path.append("../networks")
```

emmmmm..., how about files under `networks/autoencoder`? It's not elegant to add so many lines.

## Stupid but it works

Extend all paths recursively. I know it's not beautiful, but it really works.

```python
    # in _train.py (I wanna run it at path ./pipelines)
    import sys, os
    sys.path.extend([".."] + [os.path.join(root, name) for root, dirs, _ in os.walk("../") for name in dirs])
```

## Have a try

```shell
    $ cd pipelines
    $ python _train.py
```

You will see:

```shell
    batch_size = 64
    epochs = 500
    cnn_layer1
    lstm_layer1
```