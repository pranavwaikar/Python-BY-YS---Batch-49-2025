
# commands to create virtal env using conda

1. create virtual environment with conda

```
conda create -p venv python=3.13.2
conda activate venv
touch requirements.txt
```

2. Now add packages to requirements.txt & run command

```
pip install -r requirements.txt
```

3. Deactivate the virtual environment

```
conda deactivate
```