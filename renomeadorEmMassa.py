import os


def main():
    i = 0
    path = "C:/Users/Rike/Desktop/walppaper/"
    for filaname in os.listdir(path):
        myDest = " -" + str(i) + ".jpg"
        mySource =path + filaname
        myDest =path + myDest
        os.rename(mySource, myDest)
        i += 1 

if __name__ == '__main__':
    main()
