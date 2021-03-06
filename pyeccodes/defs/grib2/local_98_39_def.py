import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('componentIndex', 1))
    h.alias('mars.number', 'componentIndex')
    h.add(_.Unsigned('numberOfComponents', 1))
    h.alias('totalNumber', 'numberOfComponents')
    h.add(_.Unsigned('modelErrorType', 1))
    h.alias('local.componentIndex', 'componentIndex')
    h.alias('local.numberOfComponents', 'numberOfComponents')
    h.alias('local.modelErrorType', 'modelErrorType')
    h.add(_.Unsigned('offsetToEndOf4DvarWindow', 2))
    h.add(_.Unsigned('lengthOf4DvarWindow', 2))
    h.alias('anoffset', 'offsetToEndOf4DvarWindow')
