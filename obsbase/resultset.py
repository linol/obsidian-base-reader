import pandas as pd

from collections.abc import Iterator

class ResultSet:
    """Collection of notes returned by a view.

    ResultSet behaves like a sequence of Note objects and provides
    convenience methods for exporting the results.
    """

    def __init__(self, view, rows):
        self.view = view
        self.rows = list(rows)

    def __iter__(self) -> Iterator:
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        return self.rows[index]

    def to_dataframe(self):
        data = []
        for note in self.rows:
            row = {
                column: note.get(column)
                for column in self.view.columns
            }
            data.append(row)
        return pd.DataFrame(data)