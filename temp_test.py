# coding:utf-8


def main():
    in_file = open("./nist_sts_python/templates/template8","rb")
    line = in_file.readline()
    while line:
        line = line.replace(" ","")
        line = line.replace("\n","")
        a = int(line,2)
        print a
        line = in_file.readline()
        
if __name__ == '__main__':
    main()