import socket, sys


def get_server_details(host, port):
    # Data Place Holders
    urt_server_details = {}

    # Socket Request Message
    MESSAGE = "\377\377\377\377getstatus".encode('latin-1')

    # Get response from server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.connect((host, int(port)))
        sock.send(MESSAGE)
        response, addr = sock.recvfrom(1024)
        sock.close()
        response_lines = response.split("\n".encode('latin-1'))
    except Exception as ex:
        print(ex)
        response_lines = None


    # Retrieve the server settings
    if response_lines:
        config_string_parts = response_lines[1].split("\\".encode('latin-1'))
        urt_server_details['configs'] = {}
        for i in range(1, len(config_string_parts), 2):
            urt_server_details['configs'][config_string_parts[i].strip()] = config_string_parts[i + 1].strip()

        urt_server_details['players'] = []
        for x in range(2, (len(response_lines) - 1)):
            player_data = response_lines[x].split(" ".encode('latin-1'))
            player_dictionary = {"ping": player_data[1], "kills": player_data[0], "name": player_data[2][1:-1]}
            urt_server_details['players'].append(player_dictionary)

        return urt_server_details

    else:
        return False
