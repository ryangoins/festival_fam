from django.shortcuts import get_object_or_404, render

from . import models
# Create your views here.
def group_detail(request, pk):
    group = get_object_or_404(models.Group, pk=pk)
    members = models.Membership.objects.filter(group_id=pk)
    return render(request, 'families/group_detail.html', {'group': group,
                                                          'members': members})
