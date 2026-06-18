from obsbase import Vault

def test_view_name():
    vault = Vault("examples/obsbase_vault")
    view = vault.base("top50.base").views[0]

    assert view.name == "Tableau"

def test_view_type():
    vault = Vault("examples/obsbase_vault")
    view = vault.base("top50.base").views[0]

    assert view.type == "table"

def test_view_columns():
    vault = Vault("examples/obsbase_vault")
    view = vault.base("top50.base").views[0]

    assert view.columns == [
        "file.name",
        "Commune",
        "Population_de_référence",
        "Département",
        "Région",
        "Rang_2023",
    ]
    
def test_view_sort():
    vault = Vault("examples/obsbase_vault")
    view = vault.base("top50.base").views[0]

    assert view.sort == [
        {
            "property": "Rang_2023",
            "direction": "ASC",
        }
    ]
    
def test_view_filters():
    vault = Vault("examples/obsbase_vault")
    view = vault.base("top50.base").views[0]

    assert view.filters == {
        "and": [
            'file.folder == "villes"',
            "Rang_2023 <= 50",
        ]
    }
