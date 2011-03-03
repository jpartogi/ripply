#!/usr/bin/env python
import sys

sys.path.append('../ripply')

from ripply import model

class Person(object):
    __metaclass__ = model.ModelMeta

    name = model.Property(type="string")
    birth_date = model.Property(type="date")

class Child(Person):
    age = model.Property(type="integer")

person = Person(name='Andy', age=8)
person.save()

person = Person.find(key='2')
print person.name
print person.key
print type(person.age)

person.update_attributes(name='Joe')

#person.destroy()

