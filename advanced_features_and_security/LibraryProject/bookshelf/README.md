# Permissions and Groups Setup

Custom permissions are defined on the Book model.
Groups:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Use @permission_required('relationship_app.codename') in views to enforce permissions.
