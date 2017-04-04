import requests

token="3618601120.986d0b2.b682489c9a994619ada9c8759a3afed3"
base_url = "https://api.instagram.com/v1/"


def info():
    r_url=base_url + "users/self/?access_token=" + token
    print "requesting url for data=" + r_url
    my_info=requests.get(r_url).json()
    print "my_info is : \n\r"

    print my_info



def get_user_by_username(insta_username):
    r_url = (base_url + "users/search?q=%s&access_token=%s") %(insta_username,token)
    print "requesting url for data=" + r_url
    search_results = requests.get(r_url).json()

    print search_results

    if search_results['meta']['code']==200:
        if len(search_results['data']):
            print search_results["data"][0]["id"]
            return search_results["data"][0]["id"]
        else:
            print "User doesn't exist"
            return None
    else:
        print "request can't be completed"

    return None
    #print search_results

#get_user_by_username("abhi3454")

def get_users_recent_posts(insta_username):
    insta_user_id=get_user_by_username(insta_username)
    r_url = (base_url + "users/%s/media/recent/?access_token=%s") % (insta_user_id , token)
    print "requesting url for data=" + r_url
    recent_posts = requests.get(r_url).json()

    #print recent_posts

    if recent_posts["meta"]["code"] ==200:
        if len(recent_posts["data"]):
            print recent_posts["data"]
        else:
            print "No recents posts by this user"
    else:
        print "status code other than 200"


get_users_recent_posts("abhi3454")
