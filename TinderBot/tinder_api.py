import json

import config
import requests

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
}


def get_auth_token(fb_auth_token, fb_user_id):
    if "error" in fb_auth_token:
        return {"error": "could not retrieve fb_auth_token"}
    if "error" in fb_user_id:
        return {"error": "could not retrieve fb_user_id"}
    url = config.host + '/auth'
    req = requests.post(url,
                        headers=headers,
                        data=json.dumps(
                            {'facebook_token': fb_auth_token, 'facebook_id': fb_user_id})
                        )
    try:
        tinder_auth_token = req.json()["token"]
        headers.update({"X-Auth-Token": tinder_auth_token})
        print("You have been successfully authorized!")
        return tinder_auth_token
    except Exception as e:
        print(e)
    return {"error": "Something went wrong. Sorry, but we could not authorize you."}


def authverif():
    res = get_auth_token(config.fb_auth_token, config.fb_user_id)
    if "error" in res:
        return False
    return True


def get_updates(last_activity_date=""):
    '''
    Returns all updates since the given activity date.
    The last activity date is defaulted at the beginning of time.
    Format for last_activity_date: "2017-07-09T10:28:13.392Z"
    '''
    try:
        url = config.host + '/updates'
        r = requests.post(url,
                          headers=headers,
                          data=json.dumps({"last_activity_date": last_activity_date}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting updates:", e)


def get_recommendations():
    try:
        r = requests.get('https://api.gotinder.com/user/recs', headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting recomendations:", e)


def get_person(id):
    '''
    Gets a user's profile via their id
    '''
    try:
        url = config.host + '/user/%s' % id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get that person:", e)


def like(person_id):
    try:
        url = config.host + '/like/%s' % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not like:", e)


def dislike(person_id):
    try:
        url = config.host + '/pass/%s' % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not dislike:", e)
