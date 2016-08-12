from django.core.exceptions import ImproperlyConfigured
from crispy_forms.helper import FormHelper
from fluent_comments import appsettings
from crispy_forms.layout import Layout, Row, Field
from crispy_forms.bootstrap import InlineField


if appsettings.USE_THREADEDCOMMENTS:
    from threadedcomments.forms import ThreadedCommentForm as base_class
else:
    from .compat import CommentForm as base_class


class FluentCommentForm(base_class):
    """
    The comment form, applies various settings.
    """

    #: Helper for {% crispy %} template tag
    helper = FormHelper()
    helper.form_class = 'js-comments-form form-horizontal'
    helper.form_tag = False
    helper.label_class = 'col-sm-0'
    helper.field_class = 'col-sm-12'
    helper.form_show_labels = False



    def __init__(self, *args, **kwargs):
        super(FluentCommentForm, self).__init__(*args, **kwargs)

        # Remove fields from the form.
        # This has to be done in the constructor, because the ThreadedCommentForm
        # inserts the title field in the __init__, instead of the static form definition.
        for name in appsettings.FLUENT_COMMENTS_EXCLUDE_FIELDS:
            try:
                self.fields.pop(name)
            except KeyError:
                raise ImproperlyConfigured("Field name '{0}' in FLUENT_COMMENTS_EXCLUDE_FIELDS is invalid, it does not exist in the comment form.")

    def get_comment_create_data(self):
        # Fake form data for excluded fields, so there are no KeyError exceptions
        for name in appsettings.FLUENT_COMMENTS_EXCLUDE_FIELDS:
            self.cleaned_data[name] = ""

        return super(FluentCommentForm, self).get_comment_create_data()
