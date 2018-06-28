def generate_full_country_info():
    return client.service.FullCountryInfoAllCountries()

def print_country(country):
    country_output = country.sISOCode + "|" + country.sName + "|" + country.sCapitalCity + "|" + country.sPhoneCode + "|" + country.sContinentCode
    try:
        country_output = country_output + "|" + country.sCurrencyISOCode + "|"
    except TypeError:
        country_output = country_output + "|" + "None" + "|"

    languages = []
    for language in str(country.Languages).splitlines():
        language = language.strip()
        if language[0:2] == "sI":
            languages.append(language.split("=", maxsplit=1)[-1].replace("\"", "").strip())
    for term in languages:
       country_output = country_output + client.service.LanguageName(term) + " (" + term + "), "
    country_output = country_output[:-2]
    return country_output


import json
import csv
from suds.client import Client
with open("country_info.csv", "w"):
    pass

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = Client(url)

country_info = generate_full_country_info()
with open("country_info.csv", "a") as f:
    for country in country_info[0]:
        if country == country_info[0][-1]:
            f.write(print_country(country)) 
        else:
            f.write(print_country(country) + "\n")


 #------------------------------
# individual_country_list = []
# from collections import defaultdict
# country_big_list = []
# country_dictionary = defaultdict(list)
# country_info_list = []
# languages_list = []

# country_info_list = str(country_info).split("(tCountryInfo)")
# for country in country_info_list:
#     individual_country_list.append(country.splitlines())
# individual_country_list.pop(0) 
# for list in individual_country_list:
#     country_list = []
#     for i in range(len(individual_country_list[0])):
#         if i >= list.index(list[-1]):
#             break
#         else:
#             list[i] = list[i].strip()
#             print(list[i-1])
#             if str(list[i])[0:9] == "Languages":
#                 languages_list = []
#                 for x in range(i+4, list.index(list[-1]), 1):
#                     language = str(list[x].strip())
#                     if language[0] == "s":
#                         languages_list.append(language.split("=")[-1])
#                 country_list.append(languages_list)
#                 break
#             elif str(list[i])[0] == "s":
#                 country_list.append(str(list[i]).split("=")[-1])
#     country_big_list.append(country_list)

# for i in range(len(country_big_list)):
#     for y in range(len(country_big_list[i])):
#         temp_dictionary = {}
#         temp_dictionary["ISOCode"]= country_big_list[i][0]
#         temp_dictionary["Name"]= country_big_list[i][1]
#         temp_dictionary["CapitalCity"]= country_big_list[i][2]
#         temp_dictionary["PhoneCode"]= country_big_list[i][3]
#         temp_dictionary["ContinentCode"]= country_big_list[i][4]
#         temp_dictionary["CurrencyISOCode"]= country_big_list[i][5]
#         temp_dictionary["CountryFlag"]= country_big_list[i][6]
#         temp_dictionary["Languages"] = country_big_list[i][7]

#     country_dictionary[temp_dictionary["Name"]] = temp_dictionary

# for country in country_dictionary:
#     print("\n")
#     for info in country_dictionary[country]:
#         print(str(country_dictionary[country][info]).replace("\"", ""), "|",  end='')