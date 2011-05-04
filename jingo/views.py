from django.views.generic.base import TemplateResponseMixin
import jingo


def direct_to_template(request, template, **kwargs):
    return jingo.render(request, template, kwargs)


class JingoResponseMixin(TemplateResponseMixin):
    template_name = None
    response_class = jingo.JingoTemplateResponse
