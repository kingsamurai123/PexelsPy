from pexelsPy import API
import os
import sys
# Init api object with your Pexels API key
API_KEY = os.environ.get("PEXELS_API")
api = API(API_KEY)
page_number = sys.argv[1]
results_in_a_page = sys.argv[2]

#Page number should be >= 1 or a response errror 500 is returned. Sooooo..
if page_number == 0:
    page_number = 1

#Error 500 removal
if results_in_a_page == 0:
    results_in_a_page = 1

# Search curated photos in the fifth page
api.curated_photos(results_per_page = results_in_a_page, page = page_number)
# Loop backwards
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
        print("-----------------------------------------------\n")
    # print("Page Number: ",api.page)
    # If there is no previous page print the first page and end the loop
    # if not api.has_previous_page:
    #     print("First page: ", api.page)
    #     break
    # Search previous page
    # api.search_previous_page()
