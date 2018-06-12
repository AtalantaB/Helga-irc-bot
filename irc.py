import socket

class IRC():

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(bytes('PRIVMSG %s :%s\n' % (chan, msg),'UTF-8'))
        
    def connect(self, setDict):
        server = setDict['server']
        port = setDict['port']
        botNick = setDict['botnick']
        botDescription = setDict['botdescription']
        channels = setDict['channels']

        self.irc.connect((server, port))

        #Set username and description
        self.irc.send(bytes('USER %s %s %s :%s\n' % (botNick, botNick, botNick, botDescription), 'UTF-8'))

        #Set bot NickName
        self.irc.send(bytes('NICK %s\n' % botNick, 'UTF-8'))

        #Join each channel specified
        for chan in channels:
            self.irc.send(bytes('JOIN %s\n' % (chan if chan.startswith('#') else '#' + chan),'UTF-8'))

    def get_text(self):
        text = self.irc.recv(2040).decode('UTF-8').strip('\n\r')
        #Ping response
        if text.startswith('PING'):
            self.irc.send(bytes('PONG :pingis\n', 'UTF-8'))

        return text

    def quit(self, exitMessage = ''):
        self.irc.send(bytes('QUIT %s\n' % exitMessage, 'UTF-8'))
