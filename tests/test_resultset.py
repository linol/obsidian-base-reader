from obsbase import Vault

def test_to_dataframe():
    df = (
        Vault("examples/obsbase_vault")
        .base("top50.base")
        .run()
        .to_dataframe()
    )
    assert len(df) == 50

def test_dataframe_columns():
    df = (
        Vault("examples/obsbase_vault")
        .base("top50.base")
        .run()
        .to_dataframe()
    )
    assert list(df.columns) == [
        "file.name",
        "Commune",
        "Population_de_référence",
        "Département",
        "Région",
        "Rang_2023",
    ]
    
def test_dataframe_first_row():
    df = (
        Vault("examples/obsbase_vault")
        .base("top50.base")
        .run()
        .to_dataframe()
    )
    assert df.iloc[0]["Commune"] == "Reims"