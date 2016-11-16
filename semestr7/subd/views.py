from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from .model import *


@staff_member_required
def index(request):
    return HttpResponseRedirect("/admin/")
    # template = loader.get_template('rflocator/index.html')
    # clientdata = ClientData.objects.all().order_by('-created')[:30]
    # context = RequestContext(request, {
    #     'clientdata': clientdata,
    # })
    # return HttpResponse(template.render(context))
