import pandas as pd 


def just_street_name_lowercase(street):
    street_type = ['ct', 'circle', 'crescent', 'pl', 'ave', 'dr', 'terr', 
                    'blvd', 'cresc', 'place', 'real', 'rd', "street", "avenue",
                    "st", "road"]
    street_name = street.lower()
    split = street_name.split()
    if split[-1] in street_type:
        result = split[0]
        for phrase in split[1:-1]:
            result += (" " + phrase)
        return result
    return street_name




def get_sweeping_time(street_num, street_name):
    street_name = just_street_name_lowercase(street_name)
    if (street_name == "mlk" or street_name == "martin luther king"):
        street_name = "m l king"
    street_num = int(street_num)
    data = pd.read_csv("data/fullsweepingschedule.csv")
    data["Even?"] = (data["To"] % 2)
    even_odd = data[data["Even?"] == (street_num % 2)]
    street_sched = even_odd[even_odd["Street Name"] == street_name]
    if len(street_sched) == 0:
        return "There is no street sweeping on this street (check that you entered the street name correctly and that it's in Berkeley)"
    street_and_num = street_sched[(street_sched["From"] <= street_num) & (street_sched["To"] >= street_num)]
    if len(street_and_num) == 0:
        return "There is no street sweeping at this location."
    day_of_month = street_and_num["Day of Month"].values[0]
    time = street_and_num["Time"].values[0]
    return "Sweeping occurs on the " + day_of_month + " (" + time + ") of each month (except Holidays)"