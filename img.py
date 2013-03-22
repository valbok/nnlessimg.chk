import Image

def compareHexByteLists( list1, list2 ):
    m = len( list1 ) if len( list1 ) >= len( list2 ) else len( list2 )
    diff = 0
    for i in range( m ):
        try:
                j = int( list1[i], 16 )
        except:
                j = 0
        try:
                z = int( list2[i], 16 )
        except:
                z = 0

        diff += abs( j - z )

    y = 100 - ( diff * 100 )/( 256.0 * m )
    return y

class Img( object ):
    def __init__( self, filename ):
        self._im = Image.open( filename )

    def getHexByteList( self ):
        width, height = self._im.size
        pix = self._im.load()
        result = []
        for i in range( width ):
            for j in range( height ):
                r,g,b = pix[i,j]
                result.append( hex( r ) )
                result.append( hex( g ) )
                result.append( hex( b ) )

        return result

    def compareWith( self, image ):
        a = self.getHexByteList()
        b = image.getHexByteList()

        return compareHexByteLists( a, b )

    def compareSizesWith( self, image ):
        a = self.getHexByteList()
        b = image.getHexByteList()
        result = {}
        for index in xrange( len( a ) ):
            if index not in result:
                result[index] = {}

            for size in xrange( 1, len( a ) ):
                r1 = a[index:index + size]
                r2 = b[index:index + size]
                result[index][size] = compareHexByteLists( r1, r2 )

        return result
