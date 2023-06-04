from tkinter import *
from library_management import display_client_information, calculate_penalties, display_top_book_lovers, display_most_read_books, display_category_statistics

def display_info():
    display_client_information()

def display_penalties():
    calculate_penalties()

def display_top_lovers():
    display_top_book_lovers()

def display_most_books():
    display_most_read_books()

def display_category_stats():
    display_category_statistics()

root = Tk()

info_button = Button(root, text="Display Info", command=display_info)
info_button.pack()

penalties_button = Button(root, text="Display Penalties", command=display_penalties)
penalties_button.pack()

top_lovers_button = Button(root, text="Display Top Book Lovers", command=display_top_lovers)
top_lovers_button.pack()

most_books_button = Button(root, text="Display Most Read Books", command=display_most_books)
most_books_button.pack()

category_stats_button = Button(root, text="Display Category Statistics", command=display_category_stats)
category_stats_button.pack()

root.mainloop()
