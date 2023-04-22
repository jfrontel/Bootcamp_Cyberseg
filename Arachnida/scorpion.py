import sys
from PIL import Image
from PIL.ExifTags import TAGS

if (len(sys.argv) < 2):
    print('ERROR')
else:
    for n in sys.argv[1:]:
        file_1 = Image.open(n)
        print(file_1)
        
        # extracting the exif metadata
        exifdata = file_1.getexif()
        
        # looping through all the tags present in exifdata
        for tagid in exifdata:
            
            # getting the tag name instead of tag id
            tagname = TAGS.get(tagid, tagid)
        
            # passing the tagid to get its respective value
            value = exifdata.get(tagid)
            
            # printing the final result
            print(f"{tagname:25}: {value}")