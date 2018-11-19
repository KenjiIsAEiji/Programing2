def Txt_output():

    writeData = str()
    
    with open("C:\prog2\Program3.py") as file:
        data = file.read().split('\n')
        for i in range(len(data)):
            writeData = writeData + "%04d"%(i + 1) + " " + data[i] + "\n"
    
    with open("C:\prog2\output.txt",mode="w") as newFile:
        newFile.write(writeData)