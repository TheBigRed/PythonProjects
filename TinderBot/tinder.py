import sys
import config
import tinder_api
import tinder_helper
import json



def main(argv):

    if tinder_api.authverif() == True:
        #matches = tinder_helper.get_match_info()
        #print(json.dumps(matches, indent=4, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv)
