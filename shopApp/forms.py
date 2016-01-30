from __future__ import unicode_literals

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class MyAuthenticationForm(AuthenticationForm):
    print 'u here'
    error_messages = {
        'invalid_login': _("Please enter the correct %(username)s and password "
                           "for a staff account. Note that both fields may be "
                           "case-sensitive."),
    }

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_staff:
            print 'ehhhh',self.username_field.verbose_name
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )
