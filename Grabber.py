# Grabs messages from txt file for Discord

file1 = open("Input.txt", "r")

# Gets the content of the input file
content = file1.read()

# prints the content into the console
print(content)

# splits at motd
messages = content.split('motd: ')

# prints the motd
print(messages)

# Writes the formatted motds into the output file
with open("Output.txt", "w") as file2:
    for listitem in messages:
        file2.write('%s\n' % listitem)

