from django.forms import ModelForm

from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'status', 'members_quantity']
