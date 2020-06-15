from pexelsPy import API
import os
import sys
# Init api object with your Pexels API
API_KEY = os.environ.get("PEXELS_API")
api = API(API_KEY)

# Search Photo Variables
keyWord = str(sys.argv[1])
page_number = sys.argv[2]
results_in_a_page = sys.argv[3]

#Page number should be >= 1 or a response errror 500 is returned. Sooooo..
if page_number == 0:
	page_number = 1

#Error 500 removal
if results_in_a_page == 0:
	results_in_a_page = 1


api.search_photos(keyWord, page=page_number , results_per_page = results_in_a_page)
print("Total results: ", api.total_results)
# Loop all the pages
for _ in page_number:
    # Get all photos in the page
    photos = api.get_photos()
    # For each photo print its properties
    for photo in photos:
        print("-----------------------------------------------")
        print("Photo id: ", photo.id)
        print("Photo width: ", photo.width)
        print("Photo height: ", photo.height)
        print("Photo url: ", photo.url)
        print("Photographer: ", photo.photographer)
        print("Photo description: ", photo.description)
        print("Photo extension: ", photo.extension)
        print("Photo sizes:")
        print("\toriginal: ", photo.original)
        print("\tcompressed: ", photo.compressed)
        print("\tlarge2x: ", photo.large2x)
        print("\tlarge: ", photo.large)
        print("\tmedium: ", photo.medium)
        print("\tsmall: ", photo.small)
        print("\ttiny: ", photo.tiny)
        print("\tportrait: ", photo.portrait)
        print("\tlandscape: ", photo.landscape)
    # If there is no next page print the last page and end the loop
    if not api.has_next_page:
        print("Last page: ", api.page)
        break
    # Search next page
    api.search_next_page()
