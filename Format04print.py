##  Testing formatting with printf derivations
ruler = "0123456789012345678901234567890"
print (ruler)

### String printing is with formatter %s

#String 
s1 = "abcdef"
print ("%s" % s1)
#Right side aligment 
print ("*%10s*" % s1)
# Left side aligment 
print ("*%-10s*" % s1)


### integer printing is with formatter %d
print (ruler)

num = 4567
print ("%d" % num)
# Right align
print ("*%8d*" % num)
# Left align
print ("*%-8d*" % num)

## Float printing is with formatter %f
pi = 3.141592654
print("%f" % pi)
print("*%10.2f*" % pi)
print("*%-10.2f*" % pi)
print("*%10.3f*" % pi)
print("*%-10.3f*" % pi)
print("*%10.4f*" % pi)
print("*%-10.4f*" % pi)
print("---------")
print("*%10.2f*" % 2.718281828)  ### print from the value


pr1 = "Milk"
pr2 = "Bread"
c1 = 4.60
c2 = 9.50
print("%-15s" % "Product" + "%10s" % "Price")
print("%-15s" % pr1 + "%10.2f" % c1)
print("%-15s" % pr2 + "%10.2f" % c2)