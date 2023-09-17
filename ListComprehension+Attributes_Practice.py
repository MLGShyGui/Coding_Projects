can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# Print the key type from can_we_count_it if it has the count attribute, if not print it with a different message
print([str(type(element)) + " has the count attribute!" if hasattr(element, "count") else str(type(element)) + " does not have the count attribute :(" for element in can_we_count_it])



# Expected output
# ["<class 'dict'> does not have the count attribute :(", "<class 'str'> has the count attribute!", "<class 'int'> does not have the count attribute :(", "<class 'list'> has the count attribute!"]
