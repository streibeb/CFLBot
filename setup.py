import praw
r = praw.Reddit('OAuth CFL-GDT Ver. 3.0.0 Setup')
r.set_oauth_app_info(client_id='FY8i5bqHVJl4PtmpM-i-3Q',
                    client_secret='0a1mO_0eblhgFcuSGi7mVFBvUY_HLA',
                    redirect_uri='http://127.0.0.1:65010/authorize_callback')
								   
url = r.get_authorize_url('uniqueKey', 'submit edit read modposts privatemessages', True)
import webbrowser
webbrowser.open(url)

var_input = input("Enter uniqueKey&code: ")
access_information = r.get_access_information(var_input)
print access_information
raw_input()
