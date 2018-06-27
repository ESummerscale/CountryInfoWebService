def generate_full_country_info():
    return client.service.FullCountryInfoAllCountries()

def print_country(country):
    country_output = country.sISOCode + "|" + country.sName + "|" + country.sCapitalCity + "|" + country.sPhoneCode + "|" + country.sContinentCode
    try:
        country_output = country_output + "|" + country.sCurrencyISOCode + "|"
    except TypeError:
        country_output = country_output + "|" + "None" + "|"

    languages = str(country.Languages)
    a = json.loads(languages)
    print(a)


    # for language in str(country.Languages).splitlines():
    #     language = language.strip()
    #     try:
    #         if language[0:2] == "sI":
    #             temp = []
    #             temp.append(language.split("=", maxsplit=1)[-1].replace("\"", "").strip())
    #         if language[0:2] == "sN":
    #             temp.append(language.split("=", maxsplit=1)[-1].replace("\"", "").strip())
    #             for i in range(0, len(temp), 2):
    #                 country_output = country_output + temp[i+1] + " (" + temp[i] + "), "
    #     except IndexError:
    #         country_output = country_output + "N/A"
    # country_output = country_output[:-2]
    # print(country_output)
    # return country_output

    

import json
from suds.client import Client
from collections import defaultdict
country_big_list = []
country_dictionary = defaultdict(list)
country_info_list = []
languages_list = []


individual_country_list = []
count = 0
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = Client(url)

country_info = generate_full_country_info()

for country in country_info[0]:
    country_info_list.append(print_country(country))
# with open("country_info.csv", "w") as f:
#     for country in country_info_list:
#         f.write(country + "\n")


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