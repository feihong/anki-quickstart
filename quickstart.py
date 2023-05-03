from pathlib import Path
import re
from py_asciimath.translator.translator import ASCIIMath2Tex
import markdown

converter = ASCIIMath2Tex(log=False, inplace=False)
# input = 'sum_(i=1)^n i^3=((n(n+1))/2)^2'
input = '(-b +- sqrt(b^2 - 4ac))/(2a)'
output = converter.translate(input, displaystyle=False, from_file=False, pprint=False)
# Ignore the two $ on each side
output = output[1:-1]
# Replace consecutive braces with brace+space so as to not conflict with }} delimiter for cloze deletion
output = re.sub(r'[}]{2,}', lambda m: '} ' * len(m.group(0)), output)
print(f'AsciiMath -> TeX:\n{output}\n')

input = Path('mathjax-anki.md').read_text()
output = markdown.markdown(input)
print(f'Mardown -> HTML:\n{output}')
