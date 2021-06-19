from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from groups.models import Group
from groups.forms import GroupCreateForm

from project.utils import format_records


def get_groups(request):
    groups = Group.objects.all()

    groups_list = format_records(groups)
    return HttpResponse(groups_list)


@csrf_exempt
def create_group(request):

    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    html_form = f"""
        <form method="post">

        { form.as_p() }

        <input type="submit" value="Submit">

        </form>
        """

    response = html_form

    return HttpResponse(response)
