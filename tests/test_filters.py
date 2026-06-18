from obsbase.filters import FilterExpression


class FakeNote:

    def __init__(self):

        self.data = {
            "file.folder": "emploi/Annonces/2025",
            "Population": 120000,
        }

    def get(self, key):
        return self.data[key]


def test_startswith():

    note = FakeNote()

    expr = FilterExpression(
        'file.folder.startsWith("emploi/Annonces")'
    )

    assert expr.evaluate(note)


def test_equal():

    note = FakeNote()

    expr = FilterExpression(
        'Population == 120000'
    )

    assert expr.evaluate(note)