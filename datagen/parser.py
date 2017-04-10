# A pre-processing module for search.py to validate POST request received

from Dataset import Dataset
import decimal

# Pre-defined parameters
MAX_ROWS = 1000


# Pre-processing: Validate and Fill indicator ind for further processing
def read_request(request):
    dataset = Dataset()

    if request.POST:
        check_list = request.POST.getlist('check_list')

        if request.POST['rows']:
            rows = to_int(request.POST['rows'])
            if validate_rows(rows):
                dataset.set_rows(rows)
            # else use default value, rows = 100
        if "name" in check_list:
            dataset.set_names()
        if "gender" in check_list:
            male_percent = to_int(request.POST['male_percent'])
            female_percent = to_int(request.POST['female_percent'])
            if validate_percentage(male_percent, female_percent):
                dataset.set_gender(True, male_percent, 100 - male_percent)
            else: # use default value, 50% male, 50% female
                dataset.set_gender(50, 50)
        if "country" in check_list:
            country_name_1 = request.POST['country_name_1']
            country_percent_1 = to_int(request.POST['country_percent_1'])
            country_name_2 = request.POST['country_name_2']
            country_percent_2 = to_int(request.POST['country_percent_2'])
            if validate_percentage(country_percent_1, country_percent_2):
                if country_name_1 == country_name_2 == "No Preference":
                    dataset.set_country(True, country_name_1, 100, country_name_2, 0)
                else:
                    dataset.set_country(True, country_name_1, country_percent_1, country_name_2, country_percent_2)
            else:
                dataset.set_country(True, "No Preference", 100, "No Preference", 0)
        if "race" in check_list:
            race_name_1 = request.POST['race_name_1_id']
            race_percent_1 = to_int(request.POST['race_percent_1'])
            race_name_2 = request.POST['race_name_2_id']
            race_percent_2 = to_int(request.POST['race_percent_2'])
            if validate_percentage(race_percent_1, race_percent_2):
                if race_name_1 == race_name_1 == "No Preference":
                    dataset.set_race(True, "No Preference", 100, "No Preference", 0)
                else:
                    dataset.set_race(True, race_name_1, race_percent_1, race_name_2, 100 - race_percent_1)
            else:
                dataset.set_race(True, "No Preference", 100, "No Preference", 0)
        if "credit_card" in check_list:
            cc_name_1 = request.POST['cc_name_1_id']
            cc_percent_1 = to_int(request.POST['cc_percent_1'])
            cc_name_2 = request.POST['cc_name_2_id']
            cc_percent_2 = to_int(request.POST['cc_percent_2'])
            if validate_percentage(cc_percent_1, cc_percent_2):
                if cc_name_1 == cc_name_1 == "No Preference":
                    dataset.set_cc(True, "No Preference", 100, "No Preference", 0)
                else:
                    dataset.set_cc(True, cc_name_1, cc_percent_1, cc_name_2, 100 - cc_percent_1)
            else:
                dataset.set_cc(True, "No Preference", 100, "No Preference", 0)
    return dataset


# Converts string to int with rounding as required
def to_int(value):
    return int(round(decimal.Decimal(value)))


# Validates rows fall within valid range of values
def validate_rows(rows):
    if 0 < rows <= MAX_ROWS:
        return True
    else:
        return False


# Validate percentage pairs
def validate_percentage(percent_1, percent_2):
    # Check sum = 100% and no negative values
    if percent_1 + percent_2 == 100 \
            and percent_1 >= 0 and percent_2 >= 0:
        return True
    else:
        return False

