try:
    testFile = open("testfile.txt", "w+")
    testFile.write("my first line")
    testFile.write("this file\n")
    testFile.write("contains three lines\n")


finally:
 testFile.close()

 with open('testFile.txt', 'r', encoding='utf-8') as f:
     content = f.readlines()

 for line in content:
     print(line)
