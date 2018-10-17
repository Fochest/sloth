import requests
import json
import sloth.conf.default_config

def loadlabelgroup(labelgroup):
    response = requests.get('http://gitlab.codesupply.de:8082/api/labelgroups/'+labelgroup)
    data = response.json()
    l = []
    for label in data["labels"]:
        attribute = {}
        name = label['name']
        attribute['class'] = 'rect'
        labelJson = {}
        labelJson['attributes'] = attribute
        labelJson['inserter'] = 'sloth.items.RectItemInserter'
        labelJson['item'] = 'sloth.items.RectItem'
        labelJson['type'] = label['name']
        labelJson['hotkey'] = label['hotkey']
        labelJson['text'] = label['name']
        l.append(labelJson)
    MYLABELS = tuple(l)
    LABELS += MYLABELS

# This is sloth's default configuration.
#
# The configuration file is a simple python module with module-level
# variables.  This module contains the default values for sloth's 
# configuration variables.
#
# In all cases in the configuration where a python callable (such as a
# function, class constructor, etc.) is expected, it is equally possible
# to specify a module path (as string) pointing to such a python callable.
# It will then be automatically imported.

# LABELS
#
# List/tuple of dictionaries that defines the label classes
# that are handled by sloth.  For each label, there should
# be one dictionary that contains the following keys:
#
#   - 'item' : Visualization item for this label. This can be
#              any python callable or a module path string 
#              implementing the visualization item interface.
#
#   - 'inserter' : (optional) Item inserter for this label.
#                  If the user selects to insert a new label of this class
#                  the inserter is responsible to actually 
#                  capture the users mouse actions and insert
#                  a new label into the annotation model.
#
#   - 'hotkey' : (optional) A keyboard shortcut starting 
#                the insertion of a new label of this class.
#
#   - 'attributes' : (optional) A dictionary that defines the
#                    keys and possible values of this label
#                    class.
#
#   - 'text' : (optional) A label for the item's GUI button.
#LABELS = (
#    {
#        'attributes': {
#            'class':      'Face',
#        },
#        'inserter': 'sloth.items.RectItemInserter',
#        'item':     'sloth.items.RectItem',
#        'hotkey':   'f',
#        'text':     'Face',
#    },
#    {
#        'attributes': {
#            'class':      'rect',
#        },
#        'inserter': 'sloth.items.RectItemInserter',
#        'item':     'sloth.items.RectItem',
#        'hotkey':   'r',
#        'text':     'Rectangle',
#    }
#)