from pathlib import Path
from datetime import datetime


class FileInfo:
    """Informations sur un fichier Markdown du vault."""

    def __init__(self, path: Path, vault_path: Path):
        self._path = Path(path)
        self._vault = Path(vault_path)

    @property
    def name(self):
        """Nom sans extension."""
        return self._path.stem

    @property
    def ext(self):
        """Extension sans le point."""
        return self._path.suffix.lstrip(".")

    @property
    def filename(self):
        """Nom complet."""
        return self._path.name

    @property
    def path(self):
        """Chemin relatif au vault."""
        return self._path.relative_to(self._vault).as_posix()

    @property
    def folder(self):
        """Dossier relatif au vault."""
        return self._path.parent.relative_to(self._vault).as_posix()

    @property
    def size(self):
        """Taille du fichier en octets."""
        return self._path.stat().st_size

    @property
    def created(self):
        """Date de création (ou équivalent selon le système)."""
        stat = self._path.stat()

        if hasattr(stat, "st_birthtime"):
            return datetime.fromtimestamp(stat.st_birthtime)

        return datetime.fromtimestamp(stat.st_ctime)

    @property
    def modified(self):
        """Dernière modification."""
        return datetime.fromtimestamp(
            self._path.stat().st_mtime
        )