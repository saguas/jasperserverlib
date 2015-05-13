from ResourceDescriptor import ResourceDescriptor


class InputControlDescriptor(ResourceDescriptor):
    
    def __init__(self, resourceDescriptor=None):
        resourceDescriptor = resourceDescriptor or {}
        if not isinstance(resourceDescriptor, list):
            resourceDescriptor = [resourceDescriptor]
        super(InputControlDescriptor, self).__init__(resourceDescriptor)
        self.typeMap = ['reserved', 'None', 'dataType', 'listOfValues', 'query;queryValueColumn', 'reserved', 'listOfValues', 'query;queryValueColumn', 'listOfValues', 'query;queryValueColumn', 'listOfValues', 'query;queryValueColumn']
        self.valuesType = ['bool', 'singleSelect', 'singleSelectradio', 'multiSelectCheckbox', 'multiselect', 'singleValue', 'singleValueText', 'singleValueNumber', 'singleValueDate', 'singleValueDatetime', 'singleValueTime']

    def getOtherFields(self, typeMap):
        if typeMap < 1 or typeMap > 11:
            return None
        return self.typeMap[typeMap]