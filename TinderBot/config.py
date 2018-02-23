import fb_auth

fb_username = "android.xiii@hotmail.com"
fb_password = "Diablos07"
fb_auth_token = fb_auth.get_fb_token(fb_username, fb_password)
fb_user_id = fb_auth.get_fb_id(fb_auth_token)
host = 'https://api.gotinder.com'