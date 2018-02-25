import sys
import config
import tinder_api
import tinder_helper
import json


def main():
    total_count = 0

    if tinder_api.authverif():
        while total_count < 400:
            recs = tinder_api.get_recommendations()

            for i in range(0, len(recs['results'])):
                tinder_id = recs['results'][i]['_id']
                name = recs['results'][i]['name']
                tinder_api.like(tinder_id)
                print("liked " + name)
                tinder_helper.wait_time()
                total_count += 1

        print("liked a total of {} people".format(total_count))
    else:
        print("Authorization failed")


if __name__ == '__main__':
    main()


# print(name)
# print(len(recs['results']))
# print(json.dumps(recs, indent=4, sort_keys=True))
# print(json.len)