# f = open("demo.txt","r")
# print(f.read(11))
# print(f.tell())
# # print(f.read())
# # print(f.readline())
# # print(f.readline())

# import os
# os.remove("demo1.txt")

# f1 = open("demo1.txt","w")
# f1.write("Good Morning")

# f2 = open("demo2.txt","w")
# f2.write("Myself Ram, I am from Telangana, currently pursuing B.Tech\n")

# # for i in f:
# #     f1.write(i)

# try:
#     f = open("demo.txt")
# finally:
#     f.close()
# # This why we are making sure thatfile is closed
# # properly even if exception is raised that cause the
# # program flow to stop

# with open("demo.txt") as f:
#     f.read() #--> example
#     # your code goes here



# f = open("jerry.jpg","rb")
# f1 = open("jerry_copy.jpg","wb")
# # print(f.read())

# for i in f:
#     f1.write(i)

import os

if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("File does not exist")








# #     f = open("demo.txt","r")
# # # print(f.read())
# # # print(f.readline())
# # # print(f.readline())

# # f1 = open("demo1.txt", "w")
# # f1.write("This is a new file\n")
# # f1.write("This is a random text\n")

# # for i in f:
# #     f1.write(i)


# # try:
# #     f = open("demo.txt")
# #     your code goes here
# # finally:
# #     f.close()
# # This way we are making sure that file is closed properly even if exception is raised that cause the program flow to stop


# # with open("demo.txt") as f:
# #     f.read() #--> example
# #     #your code goes here

# # f = open("demo.txt", "r")
# # print(f.read(10))
# # print(f.tell())



# # f = open("img.png", "rb")

# # f1 = open("img_copy.png", "wb")

# # # print(f.read())

# # for i in f:
# #     f1.write(i)


# # import os

# # if os.path.exists("demo1.txt"):
# #     os.remove("demo1.txt")
# # else:
#     print("File does not exist")

