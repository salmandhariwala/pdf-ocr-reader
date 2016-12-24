import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
from wand.image import Image as wimage
import io
import urllib2

key_length_dict={}

key_length_dict['ICAPS']=8
key_length_dict['Trade Ticket']=9

key_length_dict['TRADER']=5
key_length_dict['COUNTERPARTY']=25
key_length_dict['TRADE DATE']=20
key_length_dict['COVERAGE']=15
key_length_dict['SETTLE']=15


key_length_dict['CONTACT']=20
key_length_dict['NOTES']=60
key_length_dict['Dealer Id']=5
key_length_dict['Currency']=20

key_length_dict['Calendar']=15
key_length_dict['Fixed Coupon']=7
key_length_dict['Float Int Basis']=10
key_length_dict['Float Reset Freq']=4
key_length_dict['FiXed Int. Basis']=5

key_length_dict['Fixed Adjusted']=5
key_length_dict['Cashflow Type']=5
key_length_dict['salman']=5


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    text =  pytesseract.image_to_string(image)
    text = _manipulate_result(text)
    return text

def _get_image(url):
    return Image.open(io.BytesIO(wimage(file=urllib2.urlopen(url), resolution=400).convert('jpeg').make_blob('jpeg')))


def _manipulate_result(text):

	word_result={}

	for word in key_length_dict.keys():
		try:
			size = key_length_dict[word]
			start_index = text.index(word)	+ len(word)
			end_index = start_index + size
			value = text[start_index:end_index]
			value = _remove_newline(value)
			word_result[word]=value
		except ValueError:
			print("err")

	text = _create_html(word_result)
	print(text)
	return text

def _remove_newline(value):
	if '\n' in value:
		index_ofn = value.index('\n')
		value = value[0:index_ofn]
	return value

def _create_html(word_result):
	temp = ""
	for key in word_result.keys():
		temp = temp + '<span style="background-color: #FFFF00;width: 200px"> '+key + ' </span>'+" : " + "<input type='text' value='"+word_result[key] +"'> <br />"
	return temp	

# testinng
url = "https://s3-us-west-2.amazonaws.com/salman-delete/sample.pdf"
# process_image(url)

