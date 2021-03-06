import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned_bits('groupWidths', _.Get('widthOfWidths'), _.Get('numberOfGroups')))
    h.add(_.Unsigned_bits('groupLengths', _.Get('widthOfLengths'), _.Get('numberOfGroups')))
    h.add(_.Unsigned_bits('firstOrderValues', _.Get('widthOfFirstOrderValues'), _.Get('numberOfGroups')))
    h.add(_.Sum('countOfGroupLengths', _.Get('groupLengths')))
    h.add(_.Transient('halfByte', 0))
    h.add(_.Position('offsetBeforeData'))

    if h.get_l('bitmapPresent'):
        h.add(_.Data_g1second_order_general_extended_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('firstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('keyNotPresent'), _.Get('groupWidths'), _.Get('widthOfWidths'), _.Get('groupLengths'), _.Get('widthOfLengths'), _.Get('NL'), _.Get('SPD'), _.Get('widthOfSPD'), _.Get('orderOfSPD'), _.Get('numberOfPoints')))
        h.alias('data.packedValues', 'codedValues')

        if h.get_l('boustrophedonicOrdering'):
            h.add(_.Data_apply_bitmap('preBitmapValues', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))
            h.add(_.Data_apply_boustrophedonic('values', _.Get('preBitmapValues'), _.Get('numberOfRows'), _.Get('numberOfColumns'), _.Get('numberOfPoints'), _.Get('pl')))
        else:
            h.add(_.Data_apply_bitmap('values', _.Get('codedValues'), _.Get('bitmap'), _.Get('missingValue'), _.Get('binaryScaleFactor')))

    else:

        if h.get_l('boustrophedonicOrdering'):
            h.add(_.Data_g1second_order_general_extended_packing('codedValues', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('firstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('keyNotPresent'), _.Get('groupWidths'), _.Get('widthOfWidths'), _.Get('groupLengths'), _.Get('widthOfLengths'), _.Get('NL'), _.Get('SPD'), _.Get('widthOfSPD'), _.Get('orderOfSPD'), _.Get('numberOfPoints')))
            h.add(_.Data_apply_boustrophedonic('values', _.Get('codedValues'), _.Get('numberOfRows'), _.Get('numberOfColumns'), _.Get('numberOfPoints'), _.Get('pl')))
        else:
            h.add(_.Data_g1second_order_general_extended_packing('values', _.Get('section7Length'), _.Get('offsetBeforeData'), _.Get('offsetSection7'), _.Get('unitsFactor'), _.Get('unitsBias'), _.Get('changingPrecision'), _.Get('numberOfCodedValues'), _.Get('bitsPerValue'), _.Get('referenceValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('optimizeScaleFactor'), _.Get('halfByte'), _.Get('packingType'), _.Get('grid_ieee'), _.Get('precision'), _.Get('widthOfFirstOrderValues'), _.Get('firstOrderValues'), _.Get('N1'), _.Get('N2'), _.Get('numberOfGroups'), _.Get('numberOfGroups'), _.Get('numberOfSecondOrderPackedValues'), _.Get('keyNotPresent'), _.Get('groupWidths'), _.Get('widthOfWidths'), _.Get('groupLengths'), _.Get('widthOfLengths'), _.Get('NL'), _.Get('SPD'), _.Get('widthOfSPD'), _.Get('orderOfSPD'), _.Get('numberOfPoints')))
            h.alias('codedValues', 'values')

        h.alias('data.packedValues', 'values')

    h.add(_.Simple_packing_error('packingError', _.Get('bitsPerValue'), _.Get('binaryScaleFactor'), _.Get('decimalScaleFactor'), _.Get('referenceValue'), _.Get('ieee')))
    _.Template('common/statistics_grid.def').load(h)
