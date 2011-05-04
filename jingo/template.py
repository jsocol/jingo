import jinja2
from jingo import env, render_to_string

from django.template.response import TemplateResponse


class JingoTemplateResponse(TemplateResponse):

    def resolve_template(self, template):
        if not isinstance(template, jinja2.environment.Template):
            return env.get_template(template)
        return template

    @property
    def rendered_content(self):
        template = self.resolve_template(self.template_name)
        context = self.resolve_context(self.context_data).__dict__
        content = render_to_string(self._request, template, context)
        return content
