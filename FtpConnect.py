from ftplib import FTP

def ftpConnectAndTransferFile():
    ftp=FTP()
    host="hosname.com"
    port=21
    ftp.connect(host,port)
#    print(ftp.getwelcome())
    try:
        print("Logging in..")
        ftp.login("USERname","password")
        ftp.dir()
        ftp.cwd("out")
        print("inside out folder")
        ftp.storbinary('STOR test.txt', open(r'C:\Users\Name\Desktop\test.txt','rb'))
        ftp.retrlines('LIST')
		print("File copied inside out folder")
        ftp.quit()
    except:
        "falied to login"




ftpConnectAndTransferFile()