from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from medialog.newsitemview import newsitemviewMessageFactory as _

class ISummaryView(Interface):
    """
    Summary  view interface
    """

    def test():
        """ test method"""

    def imagesize():
        """ the image size used for news item view"""


class SummaryView(BrowserView):
    """
    Summary view  browser view
    """
    implements(ISummaryView)

    def imagesize(self):
        try:
           return self.context.newsitemsize
        except AttributeError:
            return 'mini'           

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}