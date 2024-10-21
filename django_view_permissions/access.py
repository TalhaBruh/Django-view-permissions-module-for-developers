"""Checks view access for Permissions"""
METHODS = (
    'GET',
    'POST',
)


# pylint: disable=too-few-public-methods
class CheckAcess:
    """
    Checks the permissions for Request.
    """
    def __init__(self, request, permissions):
        self.request = request
        self.permissions = permissions

    def have_view_access(self):
        """
        Checks if any of the permission is true for request.
        """
        method_based = tuple(
            filter(
                lambda x: bool(x[1](self.request)),
                tuple(
                    filter(
                        lambda x: x[0] == 'method',
                        self.permissions
                    )
                )
            )
        )

        class_based = tuple(
            filter(
                lambda x: bool(x[1](self.request)()),
                tuple(
                    filter(
                        lambda x: x[0] == 'class',
                        self.permissions
                    )
                )
            )
        )
        attr_based = tuple(
            filter(
                lambda x: x[2] == getattr(self.request.user, x[1]),
                tuple(
                    filter(
                        lambda x: x[0] == 'attr',
                        self.permissions
                    )
                )
            )
        )

        allowed_permissions = tuple(
            filter(
                lambda x: self.request.method in (x[3] if len(x) == 4 else METHODS),
                attr_based
            )
        ) + tuple(
            filter(
                lambda x: self.request.method in (x[2] if len(x) == 3 else METHODS),
                method_based + class_based
            )
        )

        if any(allowed_permissions):
            return True

        return False
