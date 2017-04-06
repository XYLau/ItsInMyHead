# Used to store data from HTTP POST request to generate queries
# Validation of data is done here


class Indicator(object):
    def __init__(self):
        self.rows = 100
        self.names = [False]
        self.gender = [False]
        self.country = [False]
        self.race = [False]
        self.address = [False]
        self.cc = [False]

    # Getter methods
    def get_rows(self):
        return self.rows

    def get_names(self):
        return self.names

    def get_gender(self):
        return self.gender

    def get_country(self):
        return self.country

    def get_race(self):
        return self.race

    def get_address(self):
        return self.address

    def get_cc(self):
        return self.cc

    # Setter methods
    def set_rows(self, rows):
        self.rows = rows

    def set_names(self):
        self.names = [True]

    def set_gender(self, female_perc, male_perc):
        self.gender = [True, female_perc, male_perc]

    def set_country(self, cc1_name, cc1_perc, cc2_name, cc2_perc):
        self.country = [True, cc1_name, cc1_perc, cc2_name, cc2_perc]

    def set_race(self, race1_name, race1_perc, race2_name, race2_perc):
        self.race = [True, race1_name, race1_perc, race2_name, race2_perc]

    def set_address(self, address1_name, address1_perc, address2_name, address2_perc):
        self.address = [True, address1_name, address1_perc, address2_name, address2_perc]

    def set_cc(self):
        self.cc = [True]
