from .query import build_filter
from .resultset import ResultSet

class View:
    """
    A view defined inside a Base.
    """

    def __init__(self, base, data):
        self.base = base
        self.vault = base.vault

        self.type = data["type"]
        self.name = data["name"]
        self.filters = data.get("filters", {})
        self.columns = data.get("order", [])
        self.sort = data.get("sort", [])

    def run(self):

        filter_fn = build_filter(self)
    
        rows = [
            note
            for note in self.vault.notes()
            if filter_fn(note)
        ]
    
        return ResultSet(self, rows)