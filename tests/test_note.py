from obsbase import Vault

def test_property():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note["Commune"] == "Clichy"

def test_unknown_property():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note["Toto"] is None