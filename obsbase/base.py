import yaml

from .view import View


class Base:
    """Represents an Obsidian Base definition.

    A Base contains one or more views that can be executed against a vault.
    """

    def __init__(self, vault, path):
        self.vault = vault
        self.path = path

        with open(path, encoding="utf-8") as f:
            self.raw = yaml.safe_load(f)
        
        self.views = [
            View(self, v)
            for v in self.raw["views"]
        ]
        
    def run(self, index=0):
        """Execute a view.

        Parameters
        ----------
        index : int, default=0
            Index of the view to execute.

        Returns
        -------
        ResultSet
            Matching notes.
        """
        return self.views[index].run()
    