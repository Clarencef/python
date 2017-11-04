import urllib

def read_text():
    qoute = open('./movie_quotes.txt')
    content_of_file = qoute.read()
    print(content_of_file)
    print(id(content_of_file))
    qoute.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen(' http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly")
    connection.close()

read_text()
