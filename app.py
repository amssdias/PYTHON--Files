my_file = open('data.txt', 'r')
my_file_content = my_file.read()
print(my_file_content)
my_file.close()

my_file_writting = open('data.txt', 'w')
my_file_writting.write('Andre')
my_file_writting.close()