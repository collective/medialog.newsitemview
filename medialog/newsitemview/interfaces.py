from zope.interface import Interface
from zope import schema
from zope.interface import Interface
from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
    
class INewsitemObject(Interface):
    """Marker interface for marking an object"""
    
class IFolderObject(Interface):
    """Marker interface for marking a folder"""
    
    
class INewsItemSettings(form.Schema):
    """Adds newsitemview settings to medialog.controlpanel
        """
    form.fieldset(
        'newsitemview',
        label=(u'Newsitem'),
            fields=[
             'imagesize',
            ],
    )

    imagesize = schema.Choice(
        title = u"Default Size",
        description = u"Default Image Size",
        vocabulary='medialog.newsitemview.ImageSizeVocabulary',
    )

alsoProvides(INewsItemSettings, IMedialogControlpanelSettingsProvider)