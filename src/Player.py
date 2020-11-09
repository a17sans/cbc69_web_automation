from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

class Player:
    """Class dealing with players informartions (lastname, firstname, ranking, license number)."""


    def __init__(self):
        """Loads json xpaths file, and instanciates the web driver."""
        self.xpaths = json.load('xpaths.json')

        options = webdriver.FirefoxOptions()
        options.add_argument('enable-automation')
        
        self.driver = webdriver.Firefox(options=options)
        self.driver.get('https://www.myffbad.fr/')


    def get_player_info(self, license):
        """Inputs the license number. Clicks on the profile. Get infos."""

        # Input the license number and click enter.
        self.driver.find_element_by_xpath(self.xpaths['license_input']).send_keys(str(license)).send_keys(Keys.RETURN)
        
        # Click on the first profile.
        self.driver.find_element_by_xpath(self.xpaths['player_profile']).click()

        # Build dictionnary to return
        player_info = {}

        # Get informations
        player_info['firstname'] = self.driver.find_element_by_xpath(self.xpaths['singles_mean']).text.split(' ')[0]
        player_info['lastname'] = self.driver.find_element_by_xpath(self.xpaths['singles_mean']).text.split(' ')[1]

        player_info['singles_mean'] = self.driver.find_element_by_xpath(self.xpaths['singles_mean']).text.split(' ')[0]
        player_info['doubles_mean'] = self.driver.find_element_by_xpath(self.xpaths['doubles_mean']).text.split(' ')[0]
        player_info['mixed_doubles_mean'] = self.driver.find_element_by_xpath(self.xpaths['mixed_doubles_mean']).text.split(' ')[0]

        player_info['singles_ranking'] = self.driver.find_element_by_xpath(self.xpaths['singles_ranking']).text
        player_info['doubles_ranking'] = self.driver.find_element_by_xpath(self.xpaths['doubles_ranking']).text
        player_info['mixed_doubles_ranking'] = self.driver.find_element_by_xpath(self.xpaths['mixed_doubles_ranking']).text

        self.driver.quit()

        return player_info


if __name__ == '__main__':
    # Testing 
    p = Player()
    player_info = p.get_player_info('06627137')

    for key, value in player_info.items():
        print(f'{key}: {value}')