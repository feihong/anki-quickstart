from py_asciimath.translator.translator import ASCIIMath2Tex

converter = ASCIIMath2Tex(log=False, inplace=True)
input = 'sum_(i=1)^n i^3=((n(n+1))/2)^2'
output = converter.translate(input, displaystyle=True, from_file=False, pprint=False)
print(output)
