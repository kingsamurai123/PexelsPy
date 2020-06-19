from pexelsPy import API
from datetime import datetime
import os
import sys
# Init api object with your Pexels API
API_KEY = os.environ.get("PEXELS_API")
api = API(API_KEY)


#date initialize
date = datetime.now()

# Search Photo Variables
keyWord = str(sys.argv[1])
page_number = sys.argv[2]
results_in_a_page = sys.argv[3]

#directory variables
directory_name = date.strftime("%b-%d-%Y")   #directory name is same as the execution date
filename = date.strftime("%H-%M-%S")
filename = (filename+" PhotoSearchResults.txt")
home = os.environ.get("HOME")    #to retrieve the home directory using inbuilt home variable

#Page number should be >= 1 or a response errror 500 is returned. Sooooo..
if page_number == 0:
	page_number = 1

#Error 500 removal
if results_in_a_page == 0:
	results_in_a_page = 1

#Directory allocation and changing directory
if os.path.exists(home+'/'+directory_name):
	print("    ----------------------   Directory already exists  ---------------")
else:
	os.mkdir(home+'/'+directory_name)
	print("    ----------------------   New Directory is created  ---------------")
os.chdir(home+'/'+directory_name)
print("The Directory Location is: "+os.getcwd())

#Start the file handler
file = open(filename,"w+")

#Actual photos search
api.search_photos(keyWord, page=page_number , results_per_page = results_in_a_page)
# print("Total results: ", api.total_results)
# Loop all the pages
for _ in page_number:
	# Get all photos in the page
	photos = api.get_photos()
	# For each photo print its properties
	for photo in photos:
		file.write("Photo ID: {}\n".format(photo.id))
		file.write("Photo width: {}\n".format(photo.width))
		file.write("Photo height: {}\n".format(photo.height))
		file.write("Photo URL: {}\n".format(photo.url))
		file.write("Photographer: {}\n".format(photo.photographer))
		file.write("Photo description: {}\n".format(photo.description))
		file.write("Photo extension: {}\n".format(photo.extension))
		file.write("Photo Sizes\n")
		file.write("\tOriginal: {}\n".format(photo.original))
		file.write("\tCompressed: {}\n".format(photo.compressed))
		file.write("\tLarge2x: {}\n".format(photo.large2x))
		file.write("\tLarge: {}\n".format(photo.large))
		file.write("\tMedium: {}\n".format(photo.medium))
		file.write("\tSmall: {}\n".format(photo.small))
		file.write("\tTiny: {}\n".format(photo.tiny))
		file.write("\tPortrait: {}\n".format(photo.portrait))
		file.write("\tLandscape: {}\n\n\n".format(photo.landscape))
file.close()