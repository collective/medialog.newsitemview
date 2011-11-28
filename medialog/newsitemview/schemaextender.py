from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory

#from archetypes.markerfield.field import InterfaceMarkerField
from Products.Archetypes.public import StringField

from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.ATContentTypes.interface import IATFolder
from Products.Archetypes.atapi import SelectionWidget

from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender 
from archetypes.schemaextender.field import ExtensionField

from medialog.newsitemview.interfaces import INewsitemObject, IFolderObject

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from medialog.newsitemview.vocabulary import ImageSizeVocabulary 



_ = MessageFactory('medialog.newsitemview')


class _StringExtensionField (ExtensionField, StringField): 
    pass
    
    
# need to get vocabulary to work from vocabulary.py    

class ContentTypeExtender(object):
    """Adapter that adds custom data used for news item image size."""
    adapts(IATNewsItem)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    layer = INewsitemObject
    _fields = [
        _StringExtensionField("newsitemsize",
            schemata = "settings",
            enforceVocabulary=True,
            vocabulary = ImageSizeVocabulary(),
            default="preview",
            interfaces = (INewsitemObject,),
            widget = SelectionWidget(
                label = _(u"label_newsitemsize",
                    default=u"Size for news item image"),
                description = _(u"help_newsitemimage",
                    default=u"Choose Size"),
                ),
            ),
        ]

    def __init__(self, context):
    	self.context = context

    def getFields(self):
        return self._fields

#    def __init__(self, contentType):
#        pass

class FolderTypeExtender(object):
    """Adapter that adds custom data used for image size."""
    adapts(IATFolder)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    layer = IFolderObject
    _fields = [
        _StringExtensionField("folderimagesize",
            schemata = "settings",
            enforceVocabulary=True,
            vocabulary = ImageSizeVocabulary(),
            default="preview",
            interfaces = (INewsitemObject,),
            widget = SelectionWidget(
                label = _(u"label_folderimagesize",
                    default=u"Size for image in summary view"),
                description = _(u"help_folderimagesize",
                    default=u"Choose Size"),
                ),
            ),
        ]

        
    def __init__(self, context):
    	self.context = context

    def getFields(self):
        return self._fields

#    def __init__(self, contentType):
#        pass