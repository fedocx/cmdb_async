import paramiko

class Connect():
    def __init__(self, Ip, Username, Password, Port=22):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client = client
        self.Ip = Ip
        self.Port = Port
        self.Username = Username
        self.Password = Password

    def SSHConnect(self):
        self.client.connect(self.Ip, self.Port, self.Username, self.Password)

    def Command(self,command):
        stdin, stdout, stderr = self.client.exec_command(command)
        res =  stdout.read().decode('utf-8')
        return res