# Reusable functions for for loops

# Basic for loop function
def print_names(names):
    """Print each name in the list"""
    for i in names:
        print(i)

# For loop with else
def print_names_with_else(names):
    """Print names, show message if list is empty"""
    for i in names:
        print(i)
    else:
        print("empty list")

# For loop with break
def print_until_name(names, stop_name):
    """Print names until a specific name is found, then break"""
    for i in names:
        print(i)
        if i == stop_name:
            break

# Continue statement
def print_skip_name(names, skip_name):
    """Print names but skip a specific name"""
    for i in names:
        if i == skip_name:
            continue
        print(i)

# Pass statement
def print_with_pass(names, pass_name):
    """Print names, pass on a specific name"""
    for i in names:
        if i == pass_name:
            pass
        print(i)

# Usage examples
if __name__ == "__main__":
    names = ("sam", "derik", "john")
    
    print("Basic for loop:")
    print_names(names)
    
    print("\nFor loop with else:")
    print_names_with_else(names)
    
    print("\nFor loop with break:")
    print_until_name(("sam", "deerik", "john"), "deerik")
    
    print("\nContinue statement:")
    print_skip_name(("sam", "deerik", "john"), "john")
    
    print("\nPass statement:")
    print_with_pass(("sam", "deerik", "john"), "john")

