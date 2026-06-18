from pathlib import Path
from collections.abc import Iterator

from .note import Note
from .base import Base
from .query import build_filter

class Vault:
    """Represents an Obsidian vault.

    A vault provides access to Markdown notes and Obsidian Base files.

    Parameters
    ----------
    path : str | Path
        Path to the root directory of the vault.
    """

    def __init__(self, path):
        self.path = Path(path)

    def notes(self) -> Iterator[Note]:
        """Iterate over all Markdown notes in the vault.

        Yields
        ------
        Note
            Each Markdown note found recursively in the vault.
        """
        for file in self.path.rglob("*.md"):
            yield Note(file,self)
            
    def base(self, filename):
        """Load a Base definition.

        Parameters
        ----------
        filename : str
            Relative path to the `.base` file.

        Returns
        -------
        Base
            The loaded Base object.
        """
        return Base(self, self.path / filename)