from shh_client import CustomSSHClient
from psarchive import make_archive, glob, Unsupported_archive_exception

def main():
    try:
        make_archive('temp.zip', archive_type='rar').save(*glob('*.py'))
        print()

        ssh = CustomSSHClient('10.199.196.125',22 ,'root','abc123')
        ssh.upload('temp.zip') # sftp upload
    except Unsupported_archive_exception as err:
        print(err)

if __name__ == '__main__':
    main()