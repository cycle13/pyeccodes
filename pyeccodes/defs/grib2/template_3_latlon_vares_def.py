import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('Ni', 4))
    h.alias('numberOfPointsAlongAParallel', 'Ni')
    h.alias('Nx', 'Ni')
    h.add(_.Unsigned('Nj', 4))
    h.alias('numberOfPointsAlongAMeridian', 'Nj')
    h.alias('Ny', 'Nj')
    h.alias('geography.Ni', 'Ni')
    h.alias('geography.Nj', 'Nj')
    h.add(_.Unsigned('basicAngleOfTheInitialProductionDomain', 4))
    h.add(_.Transient('mBasicAngle', (_.Get('basicAngleOfTheInitialProductionDomain') * _.Get('oneMillionConstant'))))
    h.add(_.Transient('angleMultiplier', 1))
    h.add(_.Transient('mAngleMultiplier', 1000000))
    pass  # when block
    h.add(_.Unsigned('subdivisionsOfBasicAngle', 4))
    h.add(_.Transient('angleDivisor', 1000000))
    pass  # when block
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib2/tables/[tablesVersion]/3.3.table"))
    h.add(_.Bit('resolutionAndComponentFlags1', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags2', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('iDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('jDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 7))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 6))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 6))

    def ijDirectionIncrementGiven_inline_concept(h):
        def wrapped(h):

            iDirectionIncrementGiven = h.get_l('iDirectionIncrementGiven')
            jDirectionIncrementGiven = h.get_l('jDirectionIncrementGiven')

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 1:
                return 1

            if iDirectionIncrementGiven == 1 and jDirectionIncrementGiven == 0:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 1:
                return 0

            if iDirectionIncrementGiven == 0 and jDirectionIncrementGiven == 0:
                return 0

        return wrapped

    h.add(_.Concept('ijDirectionIncrementGiven', None, concepts=ijDirectionIncrementGiven_inline_concept(h)))

    h.alias('DiGiven', 'iDirectionIncrementGiven')
    h.alias('DjGiven', 'jDirectionIncrementGiven')
    h.add(_.Codeflag('scanningMode', 1, "grib2/tables/[tablesVersion]/3.4.table"))
    h.add(_.Bit('iScansNegatively', _.Get('scanningMode'), 7))
    h.add(_.Bit('jScansPositively', _.Get('scanningMode'), 6))
    h.add(_.Bit('jPointsAreConsecutive', _.Get('scanningMode'), 5))
    h.add(_.Bit('alternativeRowScanning', _.Get('scanningMode'), 4))

    if h.get_l('jPointsAreConsecutive'):
        h.alias('numberOfRows', 'Ni')
        h.alias('numberOfColumns', 'Nj')
    else:
        h.alias('numberOfRows', 'Nj')
        h.alias('numberOfColumns', 'Ni')

    h.alias('geography.iScansNegatively', 'iScansNegatively')
    h.alias('geography.jScansPositively', 'jScansPositively')
    h.alias('geography.jPointsAreConsecutive', 'jPointsAreConsecutive')
    h.add(_.Transient('iScansPositively', _.Not(_.Get('iScansNegatively'))))
    h.add(_.Bit('scanningMode5', _.Get('scanningMode'), 3))
    h.add(_.Bit('scanningMode6', _.Get('scanningMode'), 2))
    h.add(_.Bit('scanningMode7', _.Get('scanningMode'), 1))
    h.add(_.Bit('scanningMode8', _.Get('scanningMode'), 0))
    h.add(_.Change_scanning_direction('swapScanningX', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('xFirst'), _.Get('xLast'), _.Get('x')))
    h.alias('swapScanningLon', 'swapScanningX')
    h.add(_.Change_scanning_direction('swapScanningY', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('yFirst'), _.Get('yLast'), _.Get('y')))
    h.alias('swapScanningLat', 'swapScanningY')

    with h.list('longitudesList'):
        for i in range(0, h.get_l('Ni')):
            h.add(_.Unsigned('longitudes', 4))

    with h.list('latitudesList'):
        for i in range(0, h.get_l('Nj')):
            h.add(_.Signed('latitudes', 4))
