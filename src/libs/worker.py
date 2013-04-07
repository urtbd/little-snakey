from server import get_server_details
import time
from mem_store import PLAYER_LIST


def monitor_servers(data):
    print 'ok'

    # empty players list
    for x in data:
        PLAYER_LIST[x['address']] = []

    print PLAYER_LIST

    for x in data:
        server_data = x['address'].split(':')
        host = server_data[0]
        port = server_data[1]
        details = get_server_details(host, port)

        # Check new players
        for y in details['players']:
            if y['name'] not in PLAYER_LIST[x['address']]:
                pass

        # reset players data
        PLAYER_LIST[x['address']] = []
        for y in details['players']:
            PLAYER_LIST[x['address']].append(y['name'])

