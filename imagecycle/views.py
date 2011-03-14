from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from imagecycle.models import ImageCycle, Choice

def index(request):
	imagecycle_list = ImageCycle.objects.all()
# 	for image_set in imagecycle_list:
# 		for image in  image_set:
# 			if image.page_link:
# 				image.url = (image_page.link)

	return render_to_response('imagecycle/index.html', {'imagecycle_list': imagecycle_list})