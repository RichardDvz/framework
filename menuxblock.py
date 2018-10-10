"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class MenuXBlock(StudioEditableXBlockMixin, XBlock):
    display_name = String(display_name="Titulo de la actividad", default="Encuadre de actividad", scope=Scope.settings)
    objetivo= String(display_name="Objetivo", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Cual es el objetivo de la actividad")
    descripcion =String(display_name="Descripcion", multiline_editor='html', resettable_editor=False,
        default ="", scope=Scope.content,
        help="Describe brevemente la actividad.")
    pasos = String(display_name="Pasos a seguir", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Pasos que debe seguir el alumno para realizar la activdad y como entregarla.")
    rubrica = String(display_name="Herramienta de evaluacion", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Herramienta de evaluacion (rubrica, lista de cotejo, etc.")

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/menuxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/menuxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/menuxblock.js"))
        frag.initialize_js('MenuXBlock')
        return frag

    #Make fields editable in studio
    editable_fields = ('display_name', 'objetivo', 'descripcion', 'pasos', 'rubrica', )
