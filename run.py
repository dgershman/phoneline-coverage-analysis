import requests

root = 'http://bmlt.ncregion-na.org/main_server'
state = "NC"

county_list_request = requests.get('{}/client_interface/json/?switcher=GetFieldValues&meeting_key=location_sub_province'.format(root))
counties = county_list_request.json()

service_bodies_request = requests.get('{}/client_interface/json/?switcher=GetServiceBodies'.format(root))
service_bodies = service_bodies_request.json()

for county in counties:
    county_name = county["location_sub_province"]
    print "\n{}\n===".format(county_name)
    meetings_search_request = requests.get('{}/client_interface/json/?switcher=GetSearchResults&meeting_key=location_sub_province&meeting_key_value={}'.format(root, county_name))
    meetings = meetings_search_request.json()

    for meeting in meetings:
        for service_body in service_bodies:        
            if meeting['service_body_bigint'] == service_body["id"]:
                print service_body["name"]
            