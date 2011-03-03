from ripply.connection import Connection

class ModelBase(object):

    def __init__(self, **kwargs):
        self.props.update(kwargs)
        self.__dict__ = kwargs
        self.bucket = self.__class__._bucket()
        
    def all(self):
        pass

    @classmethod
    def find(clazz, **kwargs):
        key = kwargs['key']
        object = clazz()
        result = clazz.bucket.get(key).get_data()
        # TODO: If result is not found get out! 

        object.__dict__.update(result)
        object.__dict__.update(dict(key=key))
        return object

    def save(self):
        robject = self.bucket.new('2', data=self.props)
        #TODO: If save successful return true else return false
        robject.store()

    def destroy(self):
        key = self.key
        robject = self.bucket.get(key)
        robject.delete()  

    def update_attributes(self, **kwargs):
        print kwargs
        key = self.key
        robject = self.bucket.get(key)
        data = robject.get_data()
        data.update(kwargs)
        print data

    @classmethod
    def _client(clazz):
        clazz.client = Connection().client
        return clazz.client

    @classmethod    
    def _bucket(clazz, bucket_name=None):
        clazz.bucket_name = bucket_name
        clazz.bucket = clazz._client().bucket('person')
        return clazz.bucket

    def properties(self, properties=None):
        if properties is None: return self.props
        else: self.props = properties
        
class Property(object):
    def __init__(self, type='string', value=None):
        self.type = type
        self.value = value

class ModelMeta(type):
    def __init__(clazz, classname, supers, classdict):
        pass

    def __new__(meta, classname, supers, classdict):
        superlist = list(supers)
        [ superlist.remove(s) for s in superlist if s is object ] # To prevent method resolution problem
        
        supers = tuple(superlist)
        supers = supers + (ModelBase,)

        classdict['props'] = {}
        
        for key in classdict:
            if classdict[key].__class__ is Property: pass
#                print classdict

        return type.__new__(meta, classname, supers, classdict)


