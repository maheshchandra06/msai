# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month.
# The points are awarded as follows:
# # If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display
# the number of points awarded.

if __name__ == '__main__':
    books_purchased = int(input("Enter the number of books purchased in this month: "))

    points = 0
    if 0 < books_purchased < 4:
        points = 5
    elif 3 < books_purchased < 6:
        points = 15
    elif 5 < books_purchased < 8:
        points = 30
    elif books_purchased >= 8:
        points = 60

    print(f"Points awarded: {points}")