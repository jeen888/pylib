import configparser

config = configparser.ConfigParser()
config.read('ftp.ini')
try:
    ftp2_port = config['FTP2']['PORT']
    ftp2_ip = config['FTP2']['SERVER_IP']
    ftp2_name = config['FTP2']['USERNAME']

    print(ftp2_port)  # 22221 출력
    print(ftp2_ip)    # 111.23.56.79 출력
    print(ftp2_name)  # admin 출력
except KeyError as e:
    print(f"KeyError: {e} not found in the configuration file.")
    ftp2_port = None
    ftp2_ip = None
    ftp2_name = None

