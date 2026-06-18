from obsbase import Vault

def test_file_name():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note.file.name == "Clichy"
    
def test_file_ext():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note.file.ext == "md"
    
def test_file_folder():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note.file.folder == "villes"

def test_file_path():
    vault = Vault("examples/obsbase_vault")
    note = next(vault.notes())

    assert note.file.path == "villes/Clichy.md"