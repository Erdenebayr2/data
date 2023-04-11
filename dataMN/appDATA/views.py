from django.shortcuts import render
from django.http import StreamingHttpResponse
from WSGIREF.UTIL import FileWrapper
import mimetypes
import os

def index(request):
    return render(request, 'index.html')

def download(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'urls.txt'
    filepath base_dir + '/File/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8129
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment; filename=%s" % filename
    return response
