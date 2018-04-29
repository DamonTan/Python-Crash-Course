def count_words(filenames, missing_files=[]):
    """count the number of words of a file"""
    for filename in filenames:
        try:
            with open(filename, encoding='UTF-8') as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            #msg = "Sorry, the file " + filename + " does not exist."
            #print(msg)
            missing_files.append(filename)
        else:
            words = contents.split()
            num_words = len(words)
            print("The file " + filename + " has about " + str(num_words) + " words.")
    print("\nBelow files were not found: ")
    print(missing_files)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

count_words(filenames)
