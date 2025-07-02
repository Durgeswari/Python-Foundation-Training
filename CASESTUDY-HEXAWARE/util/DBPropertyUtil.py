import configparser

class DBPropertyUtil:
    @staticmethod
    def load_db_properties():
        config = configparser.ConfigParser()
        config.read("db.properties")
        if 'mysql' not in config:
            raise Exception("'mysql' section not found in db.properties")
        return config['mysql']
