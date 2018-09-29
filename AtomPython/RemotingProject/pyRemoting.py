import paramiko
import os
import stat

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(
    'gold.seedhost.eu', username='seedamp', password='761654Sb!', port=22
    )

stdin, stdout, stderr = (
    ssh_client.exec_command("ls /home1/seedamp/downloads/Auto/")
    )

array = []
for line in stdout.readlines():
    array.append(line.strip())

ssh_client.close()


"start ftp"
sftp = ssh_client.open_sftp()
print(sftp.listdir())

sftp.chdir("/home1/seedamp/downloads/Auto/")
sftp.stat("/home1/seedamp/downloads/Auto")


for fileattr in sftp.listdir_attr("/home1/seedamp/downloads/Auto"):
    print(stat.S_ISDIR(fileattr.st_mode))


"/home1/seedamp/downloads"

ssh_client.close()

os.path.is_dir(
    'C:\\Users\\Alex Trim\\AppData\\Local\\Programs\\'
    + 'Python\\Python36\\vcruntime140.dll'
    )

for item in array:
    print(item)
