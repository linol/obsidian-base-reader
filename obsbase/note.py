from pathlib import Path
import yaml
from .file import FileInfo

class Note:
    def __init__(self, path, vault):
        self.path = Path(path)
        self.vault = vault

        text = self.path.read_text(encoding="utf-8")

        self._metadata = {}
        self._content = text

        if text.startswith("---"):
            _, fm, content = text.split("---", 2)
            self._metadata = yaml.safe_load(fm) or {}
            self._content = content.lstrip()
        self.file = FileInfo(self.path, vault.path)

    @property
    def name(self):
        return self.path.stem

    @property
    def folder(self):
        """Nom du dossier contenant la note."""
        return self.path.parent.name

    @property
    def frontmatter(self):
        return self._metadata

    @property
    def content(self):
        return self._content

    def __getitem__(self, key):
        return self._metadata.get(key)

    def get(self, field):
        if field.startswith("file."):
            attr = field.split(".", 1)[1]
            return getattr(self.file, attr)
    
        return self[field]