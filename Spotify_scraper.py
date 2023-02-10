import os
import requests
import time
import urllib.request
from PIL import Image
from pprint import pprint
import sys
import cv2
import json




SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN='BQDQMpSn83RaGm-spfaaQ24vUgTjXFvp7ulYwV5f_COrs0f133_I3POUBwjwzZzoo6r-A9JEqfZJxWoo0FoqTl4Lis-1KlXZPkcSwU1aPbOH1qqKfbMOBWZo6xhcSpqzKfkyACtWn7ZLRFQLmq9Wv6aIutNCeymZ_fs0mpDLSpzeq_D82Hu-8L5Z6aB7r3-Uk4tilpQhlJ8'


picture_url=''
display_image = True
album = ''
artist_names = ''
track_name = ''
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    global picture_url
    global album
    global artist_names
    global track_name
    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    picture_url=json_resp['item']['album']['images'][0]['url']
    link = json_resp['item']['external_urls']['spotify']
    album = json_resp['item']['album']['name']
    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info







if __name__ == '__main__':
    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)
        urllib.request.urlretrieve(picture_url,"gfg.png")
        image = cv2.imread("gfg.png",cv2.IMREAD_ANYCOLOR)
        if(display_image):
            cv2.imshow(f"{track_name} from {artist_names} on {album}", image)
            display_image=False
        if current_track_info['id'] != current_track_id:
            # pprint(
		    # 	current_track_info,
		    # 	indent=5,
		    # )
            cv2.destroyAllWindows()
            display_image=True
            current_track_id = current_track_info['id']
        cv2.waitKey(1)
        time.sleep(1)
