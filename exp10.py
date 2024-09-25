def find_names_starting_with(names, letter):
    return [name for name in names if name.startswith(letter)]

def main():
    # Sample list of names
    names = input("Enter names: ").split(',')
    names = [name.strip() for name in names]  # Remove extra spaces

    letter = input("Enter the letter to filter by: ").upper()  # Convert to uppercase
    names_with_letter = find_names_starting_with(names, letter)
    
    # Print the result
    if names_with_letter:
        print(f"Names starting with '{letter}':", names_with_letter)
    else:
        print(f"No names start with '{letter}'.")

if __name__ == "__main__":
    main()
