import tinder_api
import tinder_helper


def main():
    total_count = 0

    if tinder_api.authverif():
        now_time = tinder_helper.get_time()
        print("Starting bot at {}".format(now_time))

        while total_count < 400:
            recs = tinder_api.get_recommendations()

            if 'results' in recs:
                for i in range(0, len(recs['results'])):
                    tinder_id = recs['results'][i]['_id']
                    name = recs['results'][i]['name']

                    if len(name) > 2:
                        tinder_api.like(tinder_id)
                        print("liked " + name)
                        tinder_helper.wait_time()
                        total_count += 1

                    else:
                        tinder_api.dislike(tinder_id)
                        print("disliked " + name)

            else:
                print("Out of recommendations")

        print("liked a total of {} people".format(total_count))
        finish_time = tinder_helper.get_time()
        print("Bot ended at {}".format(finish_time))

    else:
        print("Authorization failed")


if __name__ == '__main__':
    main()


# print(name)
# print(len(recs['results']))
# print(json.dumps(recs, indent=4, sort_keys=True))
# print(json.len)