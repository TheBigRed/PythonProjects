from datetime import date, datetime
import random
from time import sleep

import config
import tinder_api as api


def get_match_info():
    matches = api.get_updates()['matches']
    now = datetime.utcnow()
    match_info = {}
    for match in matches[:len(matches)]:
        try:
            person = match['person']
            person_id = person['_id']  # This ID for looking up person
            match_info[person_id] = {
                "name": person['name'],
                "match_id": match['id'],  # This ID for messaging
                "message_count": match['message_count'],
                "bio": person['bio'],
                "gender": person['gender'],
                "messages": match['messages'],
            }
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            # continue
    print("All data stored in variable: match_info")
    return match_info


def get_blocks():
    blocks = api.get_updates()["blocks"]
    return blocks


def wait_time():
    sleep_length = random.randint(2, 8)
    sleep(sleep_length)