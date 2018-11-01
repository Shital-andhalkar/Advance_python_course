from ftplib import FTP

ftp=FTP()
ftp.connect('10.199.196.125')
ftp.login('root','abc123')
ftp.retrlines('LIST')

ftp.close()