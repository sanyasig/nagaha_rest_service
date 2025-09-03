import configparser

# Load config
config = configparser.ConfigParser()
config.read("app/config.ini")

def get_config(section, key):
    config_value = config[section][key]
    return config_value

def get_config_section(section):
    return config[section]


secrect_config = configparser.ConfigParser()
secrect_config.read("app/secrets.ini")

def get_sercret(section, key):
    config_value = secrect_config[section][key]
    return config_value
