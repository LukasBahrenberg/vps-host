import subprocess
import getpass

# delete setup script
subprocess.run('sudo rm -rf /os.py', shell=True)

# install current nodejs version
# subprocess.run('curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -', shell=True)    
subprocess.run('sudo apt-get update', shell=True)
subprocess.run('sudo apt-get install -y nodejs', shell=True)

# get user name
user = getpass.getuser()

# reset permissions
subprocess.run('sudo chown -R {}:sudo /home/{}'.format(user, user), shell=True)

# assign env variables
gituser = input("Enter GITUSER: ")
gitemail = input("Enter GITEMAIL: ")

# setup git
subprocess.run('ssh-keygen -t ed25519 -C \"{}\"'.format(gitemail), shell=True)
subprocess.run('ssh-add ~/.ssh/id_ed25519', shell=True)
subprocess.run('git config --global user.name "{}"'.format(gituser), shell=True)
subprocess.run('git config --global user.email "{}"'.format(gitemail), shell=True)
subprocess.run('cat ~/.ssh/id_ed25519.pub', shell=True)
