#Config.py Configuration wizard.

import configparser, os, re, logging
import subprocess as sp

def clearScreen():
    tmp = sp.call('cls',shell=True)

    
def confirmChoice(config, section):            
                
    clearScreen()
    print(('\nNew Defaults\n'+
           'Default Server : %s\n' % (config['DEFAULT']['Server'])+
           'Default Port : %s\n' % (config['DEFAULT']['Port'])+
           'Default Channels : %s\n' % (config['DEFAULT']['Channels'])+
           'Default Bot Nickname : %s\n' % (config['DEFAULT']['BotNick'])+
           'Default Bot Description : %s\n' % (config['DEFAULT']['BotDescription'])
           ))
    if input('Set default options to above? (y/n):').lower() == 'y':
        return config
    else:
        customConfig(config)
            
                

    
#Set configuration to default
def defaultConfig(config):

    clearScreen()
    config['DEFAULT'] = {'Server':'chat.freenode.net',
                         'Port': int(6667),
                         'Channels':['#Helga-Bot'],
                         'BotNick':'Helga-bot',
                         'BotDescription':'This is Helga Bot, source: https://github.com/dracoliat/Helga-irc-bot'}
    return config



#Define your own configuration's
def customConfig(config):

    clearScreen()
    print('Enter Default Values below.')
    config['DEFAULT']={'Server':input('Server : '),
                       'Port': input('Port (Integers Only) : '),
                       #Set Channels to list of channels seperated by space,
                       #check if starts with # and if not, add # to start
                       #of channel name.
                       'Channels': input('Channels (seperated by spaces) : '),
                       'BotNick': input('Bot Nickname : '),
                       'BotDescription': input('Bot Description : ')}

    config = confirmChoice(config,'DEFAULT')
    return config



def configSetup():

    config = configparser.ConfigParser()
    clearScreen()
    
    #print defaults, check if user wants to change them.
    configSet = defaultConfig(config) if input((
            'First time setup wizard:\n'+
            'Default Server : chat.freenode.net\n'+
            'Default Port : 6667\n'+
            'Default Channels : #Helga-Bot\n'+
            'Default Bot Nickname : Helga-bot\n'+
            'Default Bot Description : This is Helga Bot, source: https://github.com/dracoliat/Helga-irc-bot\n'+
            'Do you want to keep these defaults? (y/n): ')).lower() == 'y' else customConfig(config)

    with open('Config.ini', 'w') as configFile:
        config.write(configFile)


def configMain():
    
    clearScreen()
    if not os.path.isfile('.\\Config.ini'):
        print('Config.ini not found, starting Config Setup Wizard...')
        configSetup()

    else:
        config = configparser.ConfigParser()
        config.read('.\\Config.ini')
        if input(('Config.ini..... CONFIRMED\n'+
                  'Do you want to use these settings?\n'+
                  'Default Server : %s\n' % (config['DEFAULT']['Server'])+
                  'Default Port : %s\n' % (config['DEFAULT']['Port'])+
                  'Default Channels : %s\n' % (config['DEFAULT']['Channels'])+
                  'Default Bot Nickname : %s\n' % (config['DEFAULT']['BotNick'])+
                  'Default Bot Description : %s\n' % (config['DEFAULT']['BotDescription'])+
                  '(y/n): ')).lower() == 'n':
            configSetup()

#code graveyard
'''
if key == 'server':
    #serverRe = re.compile(r'(.*?).(.*?).(.*)')
    while re.match(r'(.*?)\.(.*?)\.(.*)$',config[section]['Server']) == None:
        logging.warning('\nInvalid choice of server (Server: %s).\n' % (config[section]['Server']) +
                        'Server must be in format <abc.def.ghi>')
        config[section]['Server'] = input('Server : ')

if key == 'port':
    while not config[section]['Port'].isdigit():
        logging.warning('\nInvalid choice of port (Port : %s).\n' % (config[section]['Port']) +
                        'Port must be numbers only <6667>')
        config[section]['Port'] = input('Port : ')

if key == 'botnick':
    while len(config[section]['BotNick']) == 0:
        logging.warning('Please specify a bot NickName:')
        config[section]['BotNick'] = input('Bot Nickname : ')

if key == 'channels':
    while len(config[section]['Channels']) < 1:
        logging.warning('You must specify at least one channel to join.')
        config[section]['Channels'] = [chan if chan.startswith('#') else '#' + chan for chan in input('Channels (seperated by spaces) : ').split(' ')]
'''
        
