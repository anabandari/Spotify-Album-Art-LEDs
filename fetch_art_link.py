import requests
import time

from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = 'BQCblTNE-pcuzOpLJQhe8opr_P7m5XrK3uL9Bv7zUbfBbKzogdaXnn74ZpvneIedmQbEl37Fj0WcEEv5XhBC-xljROiHiKCwQlYuUFbLfm167p7YQKZCmWf3TBQzEwGNBzgagz0j7BZ8QoHxAMZtr7XWFA2rDc8OqH6kE3KDkLJyc9GNAoEkBcEaZjRjUtAY7oM783HL'


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    art_link = json_resp['item']['album']['images'][0]['url']

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
        "art_link": art_link
    }

    return current_track_info


def main():
	current_track_id = None
	while True:
	    current_track_info = get_current_track(ACCESS_TOKEN)

	    if current_track_info['id'] != current_track_id:
		    pprint(
		    	current_track_info,
		    	indent=4,
		    )
		    current_track_id = current_track_info['id']

	    time.sleep(1)


if __name__ == '__main__':
    main()