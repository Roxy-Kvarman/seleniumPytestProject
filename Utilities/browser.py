
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config import Config
import os
import subprocess








class Browser:

    driver = None

    # @classmethod
    # def get_driver(cls):
    #     if Config.browser == "firefox":
    #         cls.driver = webdriver.Firefox(executable_path=Config.firefox_driver_path)
    #         cls.driver.implicitly_wait(5)
    #         cls.driver.maximize_window()
    #     elif Config.browser == "chrome":
    #         options = Options()
    #         options.add_argument("--start-maximized")
    #         cls.driver = webdriver.Chrome(executable_path=Config.chrome_driver_pagh, options=options)
    #         cls.driver.implicitly_wait(5)
    #     return cls.driver

    # @classmethod
    # def get_driver(cls):
    #     if cls.driver is not None:
    #         return cls.driver
    #     else:
    #         if Config.browser == "firefox":
    #             cls.kill_driver_process("firefox")
    #             cls.driver = webdriver.Firefox(executable_path=Config.firefox_driver_path)
    #             cls.driver.implicitly_wait(5)
    #             cls.driver.maximize_window()
    #         elif Config.browser == "chrome":
    #             cls.kill_driver_process("chrome")
    #             options = Options()
    #             options.add_argument("--start-maximized")
    #             cls.driver = webdriver.Chrome(executable_path=Config.chrome_driver_pagh, options=options)
    #             cls.driver.implicitly_wait(5)
    #         return cls.driver
    #
    # @staticmethod
    # def kill_driver_process(process_name):
    #     data = str(subprocess.check_output(['wmic', 'process', 'list', 'brief']))
    #     try:
    #         for i in range(len(data)):
    #             process = data.split("\\r\\r\\n")[i]
    #             if process_name in process:
    #                 name = process.split()[1]
    #                 os.system("taskkill /f /im " + name)
    #     except Exception as e:
    #         pass

    @classmethod
    def get_driver(cls):
        if cls.driver is not None:
            return cls.driver
        else:
            if Config.browser == "firefox":
                # cls.kill_driver_process("firefox")
                cls.driver = webdriver.Firefox(executable_path=Config.firefox_driver_path)
                cls.driver.implicitly_wait(5)
                cls.driver.maximize_window()
            elif Config.browser == "chrome":
                # cls.kill_driver_process("chrome")
                options = Options()
                options.add_argument("--start-maximized")
                cls.driver = webdriver.Chrome(executable_path=Config.chrome_driver_pagh, options=options)
                cls.driver.implicitly_wait(5)
            return cls.driver

    @classmethod
    def kill_driver_process(cls, process_name):
        data = str(subprocess.check_output(['wmic', 'process', 'list', 'brief']))
        try:
            for i in range(len(data)):
                process = data.split("\\r\\r\\n")[i]
                if process_name in process:
                    name = process.split()[1]
                    os.system("taskkill /f /im " + name)
        except Exception as e:
            pass

