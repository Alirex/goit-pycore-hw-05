# Homeworks

Course: "Python Programming: Foundations and Best Practices 2.0"

Topic: 6. "Working with files and the modular system"

---

## Check

Go to [goit_pycore_hw_05](src/goit_pycore_hw_05) .

For each task you can see:

- task description
- task solution
- etc

You can use command `uv run` to run the task.

### Task 1

Run tests for task 1:

```shell
uv run pytest --verbose -m "task(id=1)" -k test_task
```

Run tests for all implementations of task 1:

```shell
uv run pytest --verbose -m "task(id=1)"
```

---

## Dev

### Uv install or update

https://docs.astral.sh/uv/getting-started/installation/

```bash
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh;
else
    uv self update;
fi

uv --version
```

### Ruff install or update

https://docs.astral.sh/ruff/installation/

```bash
if ! command -v ruff &> /dev/null; then
    uv tool install ruff
else
    uv tool upgrade ruff
fi
```

### Create venv

```bash
uv sync --all-packages
```

### Register pre-commit hooks

```shell
pre-commit install
```

### Run pre-commit hooks

```shell
pre-commit run --all-files
```

---

## Extra

- Why is the `.idea` folder is stored in the repository?
  - [read (UKR)](https://github.com/Alirex/notes/blob/main/notes/ignore_or_not_ide_config/ukr.md)
- Why `py.typed`
  - [mypy (ENG)](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages)
  - [typing (ENG)](https://typing.python.org/en/latest/spec/distributing.html#packaging-type-information)

### Create a new project

In case, if you need to create a new project:

```shell
rm --recursive --force src pyproject.toml &&\
uv init --package --vcs none &&\
touch src/$(basename $PWD | tr '-' '_')/py.typed &&\
uv sync
```
