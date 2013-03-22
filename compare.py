from img import *

a = Img( 'images/chars/a.jpg' )
aleft = Img( 'images/chars/aleft.jpg' )
ared = Img( 'images/chars/a.red.jpg' )
ad = Img( 'images/chars/a.dirty.jpg' )
b = Img( 'images/chars/b.jpg' )

print a.compareWith( ared )
print a.compareWith( ad )
print a.compareWith( aleft )
print a.compareWith( b )
