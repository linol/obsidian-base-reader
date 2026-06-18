# Quickstart

## Load a vault

```python
from obsbase import Vault

vault = Vault("examples/obsbase_vault")
```

---

## Read notes

```python
for note in vault.notes():
    print(note.path)
```

---

## Load a Base file

```python
base = vault.base("top50.base")
```

---

## Run a view

```python
result = base.run()
```

---

## Convert to DataFrame

```python
df = result.to_dataframe()
print(df.head())
```