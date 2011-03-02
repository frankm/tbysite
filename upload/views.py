from django.shortcuts import render_to_response, get_object_or_404
from upload.models import Cantor
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings




def success(request):
	return render_to_response('upload/success.html', {'filename': 'f'})
	
def cantor_documents(request):
	return render_to_response('upload/cantor.html', {'cantor_list': Cantor.objects.all()})
	
class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file  = forms.FileField()
	audio = forms.CharField(max_length=50)
	audio_file = forms.FileField()
	
def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			handle_uploaded_file(request.FILES['audio_file'])
			name = request.FILES['file']
# 			print 'form_options', dir(form.fields.values)
# 			print 'form_type', type(form)
			return HttpResponseRedirect('/upload/success')
	else:
		form = UploadFileForm()
	return render_to_response('upload/upload.html', {'form': form}, context_instance = RequestContext(request))

def handle_uploaded_file(f):
	print 'f', f
	print 'media_root', settings.MEDIA_ROOT
	print 'f.name', f.name
	destination = open( '%s/%s' %(settings.MEDIA_ROOT, f.name),  'wb+')
	print 'destination', destination
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()