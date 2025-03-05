import math

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages =  pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        required_pages = math.ceil(photos_count / 4)
        return cls(required_pages)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            page = self.photos[i]
            if len(page) < 4: # Ensuring only 4 photos per page
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {page.index(label) + 1}"
        else:
            return "No more free slots"


    def display(self):
        output = []
        separator = '-----------'

        for page in self.photos:
            output.append(separator)
            output.append(' '.join("[]" for _ in page))

        output.append(separator)

        return '\n'.join(output)