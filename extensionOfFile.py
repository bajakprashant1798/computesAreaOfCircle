import mimetypes
import os

path = input("Add path : ")

# print(mimetypes.MimeTypes().guess_type(path)[0])

file_name, file_extension = os.path.splitext(path)

print('file name : ', file_name)
print('extension of file is: ', file_extension)
