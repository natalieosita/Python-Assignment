# Base class
class BaldacciBook:
    def __init__(self, title, protagonist, genre, pages):
        # Attributes
        self.title = title
        self.protagonist = protagonist  
        self.genre = genre
        self.pages = pages
    
    # Method to display book information
    def display_info(self):
        return f"Title: {self.title}, Protagonist: {self.protagonist}, Genre: {self.genre}, Pages: {self.pages}"
    
    # Method to check reading progress
    def reading_progress(self, pages_read):
        if pages_read > self.pages:
            return "You've solved the mystery!"
        else:
            return f"Keep investigating! {self.pages - pages_read} pages left."

# Derived class inheriting from BaldacciBook
class MysteryEBook(BaldacciBook):
    def __init__(self, title, protagonist, genre, pages, file_size):
        # Using constructor from the parent class and adding a new attribute
        super().__init__(title, protagonist, genre, pages)
        self.file_size = file_size  # New attribute for file size
    
    # Overriding method to include file size details
    def display_info(self):
        return f"{super().display_info()}, File Size: {self.file_size}MB"

# Instantiating objects inspired by author's themes
physical_book = BaldacciBook("The Target", "Will Robie", "Thriller", 432)
ebook = MysteryEBook("End Game", "Amos Decker", "Mystery", 500, 3.5)

# Testing the methods
print(physical_book.display_info())
print(physical_book.reading_progress(200))
print(ebook.display_info())