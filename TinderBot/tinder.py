import sys
import config
import tinder_api
import tinder_helper
import json



def main(argv):

    if tinder_api.authverif() == True:
        recs = tinder_api.get_recommendations()

        for i in range(0, len(recs['results'])):
            id = recs['results'][i]['_id']
            name = recs['results'][i]['name']
            tinder_api.like(id)
            print("liked " + name)
            tinder_helper.wait_time()


            #print(name)
        #print(len(recs['results']))
        #print(json.dumps(recs, indent=4, sort_keys=True))
        #print(json.len)


if __name__ == '__main__':
    main(sys.argv)
