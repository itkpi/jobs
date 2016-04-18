import os

import pybars
import re


COMPILER = pybars.Compiler()


class TemplateIncludeProxy:
    """
    Template proxy that handles recursively include directive
    """

    INCLUDE_COMMENT = re.compile(r'{{!<[ ]*([^}]+)}}')

    def __init__(self, template_source, loader):
        self.loader = loader
        self.template = COMPILER.compile(template_source)
        self.base_template_name = self._load_base_template(template_source)

    def _load_base_template(self, template_source):
        first_line = template_source.split("\n", 1)[0]
        if self.INCLUDE_COMMENT.match(first_line):
            base_name = self.INCLUDE_COMMENT.findall(first_line)[0]
            return base_name

    def __call__(self, *args, context=None, **kwargs):
        if not context:
            context = {}
        template = self.template
        if self.base_template_name:
            template = self.loader.get_template(self.base_template_name)
            body = self.template(context, *args, **kwargs)
            context.update({"body": body})
        return template(context, *args, **kwargs)


class FSTemplateLoader:
    """
    Loads template files from the file system.
    """
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def get_template(self, name):
        """
        Loads template by name by appending the .hbs extension to it.
        Returns the proxy object that handles recursive includes for templates.
        """
        with open(os.path.join(self.base_dir, name + ".hbs"), 'r', encoding='utf8') as f:
            template_source = f.read()

        return TemplateIncludeProxy(template_source, self)


# class TemplateLoader:
#     def __init__(self, base_dir):
#         self.base_dir = base_dir
#         self.compiler = pybars.Compiler()
#
#     def get_template(self, name):
#         with open(os.path.join(self.base_dir, name + ".hbs"), 'r', encoding='utf8') as f:
#             template_source = f.read()
#         template = self.compiler.compile(template_source)
#
#         base_template = None
#         first_line = template_source.split("\n")[0]
#         if INCLUDE_COMMENT.match(first_line):
#             base_name = INCLUDE_COMMENT.findall(first_line)[0]
#             base_template, _ = self.get_template(base_name)
#         return template, base_template
#
#     def get_partials(self):
#         partials = {}
#         base_partials = os.path.join(self.base_dir, 'partials')
#         for name in os.listdir(base_partials):
#             filename = os.path.splitext(name)[0]
#             template_source = open(os.path.join(base_partials, name), 'r', encoding='utf8').read()
#             template = self.compiler.compile(template_source)
#             partials[filename] = template
#         return partials
#
#     def helpers(self):
#         return {"asset": _asset,
#                 "date": _date,
#                 "excerpt": _excerpt,
#                 "strftime": _strftime,
#                 }
