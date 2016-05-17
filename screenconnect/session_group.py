

class SessionGroup():

    def __init__(self, api, name, session_type, is_system, session_filter,
                 subgroup_expressions):
        ''' Instantiates a session group object 
        
        Arguments:
        api -- object used to enact any changes/modifications
        name -- the name defined for the Session Group
        session_type -- the enumeration used to describe the type of session
        is_system -- describes whether the Session Group is user-modifiable
        session_filter -- definition by which the group is populated
        subgroup_expressions -- criteria for any further session organization
        '''

        self.api = api
        self.name = name
        self.session_type = session_type

        self.is_system = is_system
        self.session_filter = session_filter
        self.subgroup_expressions = subgroup_expressions

    def modify(self, **kwargs):
        ''' Alter the details or settings of the session group '''
        pass

    def end(self):
        pass