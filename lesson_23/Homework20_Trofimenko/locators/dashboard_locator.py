class DashboardLocatorsCollection:
    def __init__(self):
        self.__sale_locator = ('xpath', "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[1]/a")

    @property
    def sale_locator(self):
        return self.__sale_locator
