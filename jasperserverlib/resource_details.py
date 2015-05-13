import core as jasper
import json

from core.exceptions import ResourceContentError
from core.ResourceDescriptor import ResourceDescriptor

class Details(object):
	
	def __init__(self, session, path=''):
		self.session = session
		self.path = path
		self.resource = self.session.resourcesService().resource(path)
		self.resourceDescriptor = None
		
	def details(self, expanded=True):
		#if expanded:
		self.resource.parameter('expanded', str(expanded).lower())
		details = self.resource.details().result
	
		try:
			self.resourceDescriptor = ResourceDescriptor(json.loads(details.content))
		except:
			raise ResourceContentError()
			
		return self
		
	def serverInfo(self):
		return self.resource.serverInfo().content
		
	def getDescriptor(self):
		return self.resourceDescriptor