from time import sleep

from time import sleep
from basepackage.genrics import Genrics
#from base.genrics import Genrics
from basepackage.genricsscreenshot import getScreenShot
#from base.genricscreenshot import getScreenShot
from selenium.webdriver.support.select import Select

class SearchPage(Genrics):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    location_field='location'
    Hotels_field='hotels'
    RoomType_field='room_type'
    Number_of_Rooms_field ='room_nos'
    CheckInDate_field='datepick_in'
    CheckOutDate_field='datepick_out'
    AdultsPerRoom_filed='adult_room'
    ChildernPerRoom_filed='child_room'
    search_button='Submit'
    reset_button='Reset'

 # ************************************************************************

    def locationdropdown(self, value):
        element = self.getElement('id', self.location_field)
        sel = Select(element)
        sel.select_by_value(value)

    def hotelsdropdown(self, value):
        element = self.getElement('id', self.Hotels_field)
        sel = Select(element)
        sel.select_by_value(value)

    def roomtypedropdown(self, value):
        element = self.getElement('id', self.RoomType_field)
        sel = Select(element)
        sel.select_by_value(value)

    def numberofroomsdropdown(self, value):
        element = self.getElement('id', self.Number_of_Rooms_field)
        sel = Select(element)
        sel.select_by_value(value)

    def checkindate(self, date):
        self.clickOn('id',self.CheckInDate_field)

    def checkoutdate(self,date):
        self.clickOn("id",self.CheckOutDate_field)

    def numbersofadultsPerRoom(self, value):
        element = self.getElement('id', self. AdultsPerRoom_filed)
        sel = Select(element)
        sel.select_by_value(value)

    def numberofChildernPerRoom_filed(self,value):
        element = self.getElement('id', self.ChildernPerRoom_filed)
        sel = Select(element)
        sel.select_by_value(value)





