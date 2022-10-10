def ask_number(question, low, high):
 """Poproś o podanie liczby z odpowiedniego zakresu."""
 response = None
 while response not in range(low, high):
    response = int(input(question))
 return response