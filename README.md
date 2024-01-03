## Getting Started Notes:

1. Set version with `pyenv`:

```bash
pyenv local 3.10.11
```

2. tell poetry to use correct version of python:

```bash
poetry env use $(which python)
```

3. install dependecies:

```bash
poetry install
```

4. add dependency:

```bash
poetry add pandas
```

5. done

## Jupyter Setup:

1. ensure you have `ipykernel` as dependeny
2. instantiate kernel:

```bash
poetry run python -m ipykernel --user --name NAME_OF_YOUR_KERNEL
```

3. launch jupyter notebook
4. select kernel create in step 2

## Running Helpful commands:

1. install updates (equal to `pip upgrade`):

```bash
poetry update
```

2. run tests:

```bash
poetry run pytest
```

2. open shell in poetry's virtual env:

```bash
poetry shell
```
