def lookup(dictionary, search_term):
    """
    Searches for a key in the dictionary where the search_term
    is a substring of the key (case-insensitive).

    Parameters:
        dictionary (dict): The dictionary to search in
        search_term (str): The term to search for

    Returns:
        tuple: (matching_key, corresponding_value)

    Raises:
        KeyError:
            - "search term not found" if no matches exist
            - "multiple keys found" if more than one match exists
    """

    # Convert search term to lowercase for case-insensitive comparison
    search_term_lower = search_term.lower()

    # List to store matching keys
    matches = []

    # Iterate through dictionary keys
    for key in dictionary:
        # Check if search term is a substring of the key (case-insensitive)
        if search_term_lower in key.lower():
            matches.append(key)

    # If no matches found
    if len(matches) == 0:
        raise KeyError("search term not found")

    # If multiple matches found
    if len(matches) > 1:
        raise KeyError("multiple keys found")

    # Exactly one match found
    matched_key = matches[0]
    return matched_key, dictionary[matched_key]


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    fruit = {
        "apple": 1,
        "banana": 2,
        "grapefruit": 3
    }

    # Single match
    print(lookup(fruit, "NANA"))       # ('banana', 2)

    # No match example
    # print(lookup(fruit, "orange"))   # Raises KeyError("search term not found")

    # Multiple match example
    # print(lookup(fruit, "ap"))       # Raises KeyError("multiple keys found")