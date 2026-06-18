def build_filter(view):

    filters = view.filters.get("and", [])

    def match(note):

        for f in filters:

            # file.folder == "villes"
            if f.startswith("file.folder"):
                _, value = f.split("==")
                value = value.strip().strip('"')

                if note.file.folder != value:
                    return False

            # Rang_2023 <= 50
            elif "<=" in f:
                key, value = f.split("<=")

                key = key.strip()
                value = int(value.strip())

                if int(note[key]) > value:
                    return False

        return True

    return match