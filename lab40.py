# pip install pillow
from urllib2 import urlopen
from PIL import Image
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
url = 'https://www.cwb.gov.tw/V7/HotNews/Upload/2018_FLORA03.jpg'
fileToSave = urlopen(url, context=context)
origImage = Image.open(fileToSave)
origImage.save('.\\data\\orig.jpg')
half = (origImage.size[0] / 2, origImage.size[1] / 2)
halfImage = origImage.resize(half)
halfImage.save('.\\data\\half.jpg')
r90 = origImage.transpose(Image.ROTATE_90)
r90.save('.\\data\\r90.jpg')
r180 = origImage.transpose(Image.ROTATE_180)
r180.save('.\\data\\r180.jpg')
r270 = origImage.transpose(Image.ROTATE_270)
r270.save('.\\data\\r270.jpg')
