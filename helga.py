''' Main function for launching and controlling bot'''
from irc import *
from configWizard import *
import sys, os, re, configparser, logging

#Set irc to class defined in irc.py and set host to empty.
irc = IRC()
host = ''

#initalize settings
configMain()
readConfig = configparser.ConfigParser()
try:
    readConfig.read('.\\Config.ini')
except:
    logging.error('Configuration File not found, shutting down Error (001) ...')
    sys.exit()

settings = {}
for key in readConfig['DEFAULT']:
    settings[key] = readConfig['DEFAULT'][key] if key in ['server','botnick','botdescription'] else \
                    int(readConfig['DEFAULT'][key]) if key == 'port' else \
                    readConfig['DEFAULT'][key].split(' ')

#run until host is found.
def start():

    #Connect to server using .connect function from irc.py
    irc.connect(settings)
    
    global host
    while not host:
        text = irc.get_text()
        print(text)
        if text.split(' ')[1] == 'JOIN':
            host = text.split(' ')[0]
            main()

#Main loop to receive text and print it
def main():

    #Enter loop
    while 1:
        
        text = irc.get_text()
        #Don't print Ping requests.
        if not text.startswith('PING :'):
            print(text)


start()
#TODO:
#Establish connection to server - DONE
#Receive text and print - DONE
#Setup .ini file for initial configuration.
#Respond to basic commands - WIP
