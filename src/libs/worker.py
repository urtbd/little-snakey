from .server import get_server_details
from .mem_store import PLAYER_LIST


def monitor_servers(data):
    notifications = []

    # empty players list
    for x in data:
        if not x['address'] in PLAYER_LIST.keys():
            PLAYER_LIST[x['address']] = []

    # print PLAYER_LIST #### TODO: Debug

    for x in data:
        server_data = x['address'].split(':')
        host = server_data[0].encode('utf-8')
        port = server_data[1].encode('utf-8')
        details = get_server_details(host, port)

        if details:
            # Check new players
            for y in details['players']:
                if y['name'] not in PLAYER_LIST[x['address']]:
                    notifications.append("{} entered {}".format(y['name'], x['name']))

            # reset players data
            PLAYER_LIST[x['address']] = []
            for y in details['players']:
                PLAYER_LIST[x['address']].append(y['name'])

    return notifications
