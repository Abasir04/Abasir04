def leap_year_calculator(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print('its a leap year')
                return True
            else:
                # print('its not a leap year')
                return False
        else:
            # print('its a leap year')
            return True
    else:
        # print('its not a leap year')
        return False

