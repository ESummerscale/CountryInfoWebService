from suds.client import Client
from suds.transport import TransportError

def get_full_country_list():
    url = "http://webservices.oorsprong.org/websamples.countryinfo/.wso?WSDL"
    try:
        client = Client(url)
        countries_result = client.service.FullCountryInfoAllCountries()
        return countries_result[0]
    except TransportError:
        raise WebServiceError("Web service " + url + " is not available or returns error")

def print_country(country):
    country_output = country.sISOCode + "|" + country.sName + "|" + country.sCapitalCity + "|" + country.sPhoneCode + "|" + country.sContinentCode
    if country.sCurrencyISOCode:
        country_output = country_output + "|" + country.sCurrencyISOCode
    else:
        country_output = country_output + "|None"

    languages = country.Languages[0]
    if (isinstance(languages, list)):
        language_output = ','.join(language.sName for language in languages)
        country_output = country_output + "|" + language_output
    else:
        country_output = country_output + "|" + "None"
    return country_output  

class Error(Exception):
    pass

class WebServiceError(Error):
    def __init__(self, msg):
        self.msg = msg

country_list = get_full_country_list()
country_list_output = '\n'.join(print_country(country) for country in country_list)

with open("country_info.csv", "w") as f:
    f.write(country_list_output)
