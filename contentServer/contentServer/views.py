from django.http import HttpResponse
import datetime
from django import template
from django.template.loader import get_template


def hello(request):
	return HttpResponse("Hello World")
	
	
def my_homepage_view(request):
	return HttpResponse("Homepage")
	
def current_datetime(request):
	now = datetime.datetime.now()
	html = "It is not %s. "%now
	return HttpResponse(html)
	
def hours_ahead (request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+ datetime.timedelta(hours=offset)
	html = " In %s hour(s). it will be %s."%(offset, dt)
	return HttpResponse(html)
	
def name (request, username):

	t = template.Template('My name is {{name}}')
	c = template.Context({'name': username})
	
	html=t.render(c)
	return HttpResponse(html)

class Image:
	def __init__(self, id, dateModified, contents, history):
		self.id=id
		self.dateModified=dateModified
		self.contents=contents
		self.history=history
	
	
def image (request, offset):
	history1=['downloaded 1', 'downloaded2 ', 'downloaded3']
	img1=Image(id=1223, dateModified='2015-03-15', contents='image contents', history=history1)
	#img1.id=1223
	#img.dateModified='2015-03-15'
	#img1.contents='image contents'
	imgDic={}
	
	try:
	
		imgDic[img1.id]=img1
	
	
		#find the image
		t = template.Template('Image found {{img.id}}, date {{img.dateModified}}, contents {{img.contents}},{% for entry in img.history %}{{entry}}, 		{% endfor %}')
		
		
		retImg = imgDic[int(offset)]
		html=''
		c = template.Context({'img': retImg})
		html = t.render(c)
	except KeyError:
		html='image not found'
	return HttpResponse(html)
	
def imageTmp (request, offset):
	history1=['downloaded 1', 'downloaded2 ', 'downloaded3']
	img1=Image(id=1223, dateModified='2015-03-15', contents='image contents', history=history1)
	#img1.id=1223
	#img.dateModified='2015-03-15'
	#img1.contents='image contents'
	imgDic={}
	
	try:
	
		imgDic[img1.id]=img1
	
	
		#find the image
		t = get_template('imgTemplate.html')
		
		
		retImg = imgDic[int(offset)]
		html=''
		c = template.Context({'img': retImg})
		html = t.render(c)
	except KeyError:
		html='image not found'
	return HttpResponse(html)