"""Manages the communication with the API"""

import station_network.urequests as urequests
import ujson
from data.data_manager import delete_data_file

def test_get_api_data():
    """Test if the station is connected to Internet by calling an API"""

    response = urequests.get("https://upsidedownweatherapi.herokuapp.com/api/get_last_n/")
    if response != None:
        response = response.json()
        print(response)
    return None


def send_data_to_api():
    """When called, send all the datas inside the data file. If the operation worked, the datas are deleted"""

    data_file = open('data/data.txt', 'r')  

    data = "["

    for e in data_file:
        data += e.strip('\n') + ","

    data = data.strip(',')
    data += "]"

    # print(ujson.loads(data))
    
    response = urequests.post(
        "https://spookteo-api.herokuapp.com/api/v0/record",
        headers={
            "X-Access-User": "pulsar",
            "X-Access-Key": "82e08e7c7ba9c081e68741b3768ced6388c6fe421ab824f2e6e1994a1f88b3da",
            "Content-Type": "application/json"
        },
        data = str(data)
    )

    if response != None:
        response = response.json()
        print(response)
        if response["status"] == "ok":
            print("The data have been successfully sent to the API. Datas are being deleted...")
            delete_data_file()
            return True

    print("An error occured while sending datas to API. Datas will not be deleted")
    return False