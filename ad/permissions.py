from rest_framework.permissions import BasePermission

from ad.models import Selection


class SelectionActionsPermission(BasePermission):
	message = 'You do not have permission to do this'

	def has_permission(self, request, view):
		try:
			selection = Selection.objects.get(id=view.kwargs['pk'])
		except Selection.DoesNotExist:
			return False

		return selection.owner.id == request.user.id
