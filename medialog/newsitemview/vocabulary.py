from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility 
from zope.schema.interfaces import IVocabularyFactory 
from zope.app.component.hooks import getSite



def ImageSizeVocabulary():
    #Cant get this to work, so I stick with 3 sizes for now
    #portal_properties = getToolByName(object, 'portal_properties', None)
    #sizes = portal_properties.imaging_properties.getProperty('allowed_sizes')  
    #terms = [title=pair for pair in sizes ]
    return ['thumb', 'mini', 'preview', 'large', 'none']  
        
