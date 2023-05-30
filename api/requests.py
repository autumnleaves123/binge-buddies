import requests

# Set up the API endpoint URL
base_url = "https://api.tvmaze.com"

# Function to fetch TV show details by show ID
def get_tv_show_details(show_id):
    # Make the API request to retrieve show details
    response = requests.get(f"{base_url}/shows/{show_id}")
    
    # Check if the request was successful
    if response.status_code == 200:
        show_data = response.json()
        # Extract the desired information from the response
        show_title = show_data.get("name")
        show_summary = show_data.get("summary")
        show_genres = show_data.get("genres")
        
        # Print or process the extracted data as per your requirements
        print("Title:", show_title)
        print("Genres:", show_genres)
        print("Summary:", show_summary)
    else:
        print("Error:", response.status_code)
        

# Example usage
show_id = 1  # Replace with the desired TV show ID
get_tv_show_details(show_id)

'''
Example JSON for GOT:
{
    "score":1.4271401
    "show":{
        "id":82,
        "url":"https://www.tvmaze.com/shows/82/game-of-thrones",
        "name":"Game of Thrones",
        "type":"Scripted",
        "language":"English",
        "genres":["Drama","Adventure","Fantasy"],
        "status":"Ended",
        "runtime":60,
        "averageRuntime":61,
        "premiered":"2011-04-17",
        "ended":"2019-05-19",
        "officialSite":"http://www.hbo.com/game-of-thrones",
        "schedule":{
            "time":"21:00",
            "days":["Sunday"]
        },
        "rating":{"average":8.9},
        "weight":99,
        "network":{
            "id":8,
            "name":"HBO",
            "country":{
                "name":"United States",
                "code":"US",
                "timezone":"America/New_York"},
            "officialSite":"https://www.hbo.com/"
        },
        "webChannel":null,
        "dvdCountry":null,
        "externals":{
            "tvrage":24493,
            "thetvdb":121361,
            "imdb":"tt0944947"
        },
        "image":{
            "medium":"https://static.tvmaze.com/uploads/images/medium_portrait/190/476117.jpg",
            "original":"https://static.tvmaze.com/uploads/images/original_untouched/190/476117.jpg"
        },
        "summary":"<p>Based on the bestselling book series <i>A Song of Ice and Fire</i> by George R.R. Martin, this sprawling new HBO drama is set in a world where summers span decades and winters can last a lifetime. From the scheming south and the savage eastern lands, to the frozen north and ancient Wall that protects the realm from the mysterious darkness beyond, the powerful families of the Seven Kingdoms are locked in a battle for the Iron Throne. This is a story of duplicity and treachery, nobility and honor, conquest and triumph. In the <b>Game of Thrones</b>, you either win or you die.</p>",
        "updated":1658720459,
        "_links":{
            "self":{"href":"https://api.tvmaze.com/shows/82"},
            "previousepisode":{"href":"https://api.tvmaze.com/episodes/1623968"}
        }
    }
}
'''