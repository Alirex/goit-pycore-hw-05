# Homeworks

Course: "Python Programming: Foundations and Best Practices 2.0"

Topic: 8. "Functional Programming and Python Built-In Modules"

---

## Check

Go to [goit_pycore_hw_05](src/goit_pycore_hw_05) .

For each task you can see:

- task description
- task solution
- etc

You can use command `uv run` to run some task solutions.

### Task 1

Check the source code of the main implementation:

- [main.py](src/goit_pycore_hw_05/task_1/main.py)

Run tests for the main implementation:

```shell
uv run pytest --verbose -m "task(id=1)" -k test_task
```

Run tests for all implementations:

```shell
uv run pytest --verbose -m "task(id=1)"
```

### Task 2

Check the source code:

- [main.py](src/goit_pycore_hw_05/task_2/main.py)

Run tests:

```shell
uv run pytest --verbose -m "task(id=2)"
```

### Task 3

Check the source code:

- [main.py](src/goit_pycore_hw_05/task_3/main.py)
- and [related files](src/goit_pycore_hw_05/task_3)

Run tests:

```shell
uv run pytest --verbose -m "task(id=3)"
```

Run the task for the summarized data:

```shell
uv run task_3 files_default/task_3/logfile.log
```

Run the task for the log level:

```shell
uv run task_3 files_default/task_3/logfile.log error
```

Also, CLI help is available:

```shell
uv run task_3 --help
```

### Task 4

Check the source code of the decorator implementation:

- [input_error.py](src/goit_pycore_hw_05/task_4/services/input_error.py)

Run the app with automated interaction:

```shell
bash src/goit_pycore_hw_05/task_4/tests/test_interaction.sh
```

Details: [script](src/goit_pycore_hw_05/task_4/tests/test_interaction.sh)

Run the app manually:

```shell
uv run task_4
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

- Why is the `.idea` folder is partially stored in the repository?
  - [read (UKR)](https://github.com/Alirex/notes/blob/main/notes/ignore_or_not_ide_config/ukr.md)
- Why `py.typed`
  - [mypy (ENG)](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages)
  - [typing (ENG)](https://typing.python.org/en/latest/spec/distributing.html#packaging-type-information)

### Create a new project

In case, if you need to create a new project with `src-layout` instead of default, created by PyCharm,
use the following command inside the project directory:

```shell
rm --recursive --force src pyproject.toml &&\
uv init --package --vcs none &&\
touch src/$(basename $PWD | tr '-' '_')/py.typed &&\
uv sync
```
