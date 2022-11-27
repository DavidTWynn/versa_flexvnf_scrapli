from versa_flexvnf_scrapli.versa_flexvnf import VersaFlexVNFDriver

import logging
import json
import os

# Get a new set of logs each time
try:
    os.remove("scrapli.log")
    os.remove("scrapli_channel.log")
except FileNotFoundError:
    pass

logging.basicConfig(filename="scrapli.log", level=logging.DEBUG)


def remove_last_line(input: str) -> str:
    return "\n".join(input.split("\n")[:-1])


def result_to_dict(input: str) -> dict:
    return json.loads(remove_last_line(input))


def run_versa_commands():
    with open("settings.json", "r") as f:
        settings = json.loads(f.read())

    my_device = {
        "host": settings["lab_device"]["host"],
        "auth_username": settings["lab_device"]["auth_username"],
        "auth_password": settings["lab_device"]["auth_password"],
        "auth_strict_key": False,
        "transport": "ssh2",
    }

    with VersaFlexVNFDriver(
        **my_device, channel_log="scrapli_channel.log"
    ) as conn:
        response = conn.send_command("show system detail | display json")
        response.raise_for_status()
        print(result_to_dict(response.result))
        conn.acquire_priv("configuration")


if __name__ == "__main__":
    run_versa_commands()
