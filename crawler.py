from urllib.request import urlopen
import json, re

def downloadStops(id, lines):
    stops = []
    en_stops_dict = {}
    data = str(id)+"_,"+lines
    ### get en stop and build dictionary
    url = 'http://122.146.229.210/bus/NewAPI/RealRoute.ashx?Data='+data+'&Lang=En&type=GetStop'
    with urlopen(url) as f:
        try:
            stops_data = json.loads(f.read().decode('utf-8'))
            for stop in stops_data:
                en_stops_dict[stop['seqNo']] = stop['nameZh']
        except ValueError:
            print()
    ### get zh stop and bind en dict to generate zh/en stop list
    url = 'http://122.146.229.210/bus/NewAPI/RealRoute.ashx?Data='+data+'&Lang=Zh&type=GetStop'
    with urlopen(url) as f:
        try:
            stops_data = json.loads(f.read().decode('utf-8'))
            for stop in stops_data:
                stop_data = {}
                stop_data['sequence'] = stop['seqNo']
                stop_data['zh'] = stop['nameZh']
                stop_data['en'] = en_stops_dict[stop['seqNo']]
                stops.append(stop_data)
        except ValueError:
            print('%s route %s no data has'%(id, lines))
    return stops           

stopsOfRoutes = []
routes = []
en_routes_dict = {}
enRouteUrl = "http://122.146.229.210/bus/NewAPI/RealRoute.ashx?Lang=En&type=GetRoute"
zhRouteUrl = "http://122.146.229.210/bus/NewAPI/RealRoute.ashx?Lang=Zh&type=GetRoute"
### build english route name dictionary for later translate
with urlopen(enRouteUrl) as f:
    routes_exists = {}
    routes_data = json.loads(f.read().decode('utf-8'))
    for route in routes_data:
        if route['ID'] not in routes_exists:
            routes_exists[route['ID']] = 0
            en_routes_dict[route['ID']] = route['nameZh']
### get chinese route name and get stops than generate en/zh routes list
with urlopen(zhRouteUrl) as f:
    routes_exists = {}
    routes_data = json.loads(f.read().decode('utf-8'))
    for route in routes_data:
        if route['ID'] not in routes_exists:
            print('get %s'%route['nameZh'])
            route_data = {}
            route_name = {}
            routes_exists[route['ID']] = 0
            route_data['id'] = route['ID']
            route_name['zh'] = route['nameZh']
            route_name['en'] = en_routes_dict[route['ID']]
            route_data['routeName'] = route_name
            route_data['goRouteStops'] = downloadStops(route['ID'], "1")
            if route['routes'] == "2":
                route_data['backRouteStops'] = downloadStops(route['ID'], "2")


            routes.append(route_data)

with open(("kaohsiung_stopOfRoute.json"), 'w', encoding='utf8') as fp:
    print('ouput Kaohsiung bus routes')
    fp.write(json.dumps(routes, ensure_ascii=False))

print("=== complete ===")
