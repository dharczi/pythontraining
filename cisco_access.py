import paramiko
import getpass

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

device = {
    "hostname" : 'sbx-nxos-mgmt.cisco.com',
    "port" : 8181,
    "username" : 'admin',
    "password" : getpass.getpass('password> '),
    "look_for_keys" : False,
    "allow_agent" : False
}

