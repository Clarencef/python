def read_text():
    qoute = open('./movie_quotes.txt')
    content_of_file = qoute.read()
    print(content_of_file)
    print(id(content_of_file))
    qoute.close()
read_text()
