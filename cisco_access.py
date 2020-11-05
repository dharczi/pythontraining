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

try:
    ssh_client.connect(**device)
    stdin, stdout, stderr = ssh_client_exec_command('sh version')
    output = stdout.read().decode()
    print(output)
finally:
    ssh_client.close()