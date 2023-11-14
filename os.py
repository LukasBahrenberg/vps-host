import subprocess

## user setup
# create new user
user = input("Enter user name: ")
subprocess.run('adduser --disabled-password --gecos \"\" {}'.format(user), shell=True)
subprocess.run('usermod -aG sudo {}'.format(user), shell=True)

# set password hash, use pwd.py script on seperate machine to generate password
passwordhash = input("Enter user password hash: ")
subprocess.run('printf \'{}:{}\' | sudo chpasswd --encrypted'.format(user, passwordhash), shell=True)

## installations
# updates & upgrades
subprocess.run('apt-get update', shell=True)
subprocess.run('apt-get upgrade -y', shell=True)
subprocess.run('apt update', shell=True)
subprocess.run('apt upgrade -y', shell=True)

# install dev dependencies
subprocess.run('apt install -y build-essential', shell=True)
subprocess.run('apt install -y libssl-dev', shell=True)
subprocess.run('apt install -y whois', shell=True)
subprocess.run('apt-get install -y pkg-config', shell=True)
subprocess.run('apt-get install -y libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev libasound2', shell=True)

# install fail2ban
subprocess.run('apt install -y fail2ban', shell=True)
subprocess.run('apt-get install -y git', shell=True)

# install current nodejs version
subprocess.run('curl -fsSL https://deb.nodesource.com/setup_current.x | -E bash -', shell=True)    
subprocess.run('apt-get update', shell=True)
subprocess.run('apt-get install -y nodejs', shell=True)

# install docker 
subprocess.run('apt install -y software-properties-common', shell=True)
subprocess.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg', shell=True)
subprocess.run('add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"', shell=True)
subprocess.run('apt update', shell=True)
subprocess.run('apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin', shell=True)

# setup ufw
subprocess.run('ufw logging on', shell=True)
subprocess.run('ufw allow 22', shell=True) #ssh
subprocess.run('ufw --force enable', shell=True)

# setup fail2ban
subprocess.run('systemctl enable fail2ban', shell=True)
subprocess.run('systemctl start fail2ban', shell=True)
subprocess.run('systemctl status fail2ban', shell=True)

# git repo
subprocess.run('git clone https://github.com/LukasBahrenberg/vps-host.git /home/{}/ubuntu-workstation'.format(user), shell=True)

# reset permissions
subprocess.run('chown -R {}:sudo /home/{}'.format(user, user), shell=True)

# switch to user
subprocess.run('su - {}'.format(user), shell=True)
