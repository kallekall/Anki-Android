import os
import zipfile

# This script extract localization from ankidroid.zip into the right folders.
# http://crowdin.net/download/project/ankidroid.zip

# TODO
# Add GNU-GPL header to files
# Insert 0,1,2,3,4,5 values that are missing from Crowdin

# Below is the list of official AnkiDroid localizations.
# Add a language if it is more than 50% translated.
languages = ['pt-PT', 'fr', 'ru', 'ca', 'es-ES', 'el'];


zip = zipfile.ZipFile("ankidroid.zip", "r")

for language in languages:
	androidLanguage = language[:2] # Example: pt-PT becomes pt
	valuesDirectory = "../res/values-" + androidLanguage + "/"

	# Create directory if it does not exist yet.
	if not os.path.isdir(valuesDirectory):
		os.mkdir(valuesDirectory)

	# Copy localization files
	file(valuesDirectory + 'arrays.xml', 'w').write(zip.read(language + "/arrays.xml"))
	file(valuesDirectory + 'strings.xml', 'w').write(zip.read(language + "/strings.xml"))

