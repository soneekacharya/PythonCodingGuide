""" Build a logging system using the Factory Design Pattern. Create a LoggerFactory class that generates different types of loggers 
(e.g., FileLogger, ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to their respective destinations. 
Show how the Factory Design Pattern helps to decouple the logging system from the application and allows for flexible log handling. """

from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"File Log: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

class DatabaseLogger(Logger):
    def log(self, message):
        print(f"Database Log: {message}")

class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()

if __name__ == "__main__":
    logger_type = 'file'  
    logger = LoggerFactory.create_logger(logger_type)
    logger.log("This is a log message.")
