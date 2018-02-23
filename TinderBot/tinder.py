import sys
import config
import tinder_api


def main(argv):

    tinder_api.get_auth_token(config.fb_auth_token, config.fb_user_id)


if __name__ == '__main__':
    main(sys.argv)
