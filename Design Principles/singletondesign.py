class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = {} 
        return cls._instance
    
    def load_configuration(self) -> None:
        self.setting1 = "value1"

    def get_setting(self, key):
        return self.config.get(key)

if __name__ == "__main__":
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    print(config_manager1.get_setting("setting1"))  
    print(config_manager2.get_setting("setting2"))  

    print(config_manager1 is config_manager2)