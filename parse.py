"""
Parsing by lines probably doesn't make sense because math blocks probably need to occupy multiple lines
"""
from pathlib import Path
import re
import io
from dataclasses import dataclass

input_file = Path('example.notes')
output_file = input_file.with_suffix('.md')

def get_lines():
  with input_file.open('r', encoding='utf8') as fp:
    for line in fp:
      line = line.strip()
      if line:
        yield line

      
@dataclass
class Header:
  level: int
  content: str

@dataclass
class CardSeparator: pass

@dataclass
class Block:
  content: list

@dataclass
class Math:
  content: str

@dataclass
class MathBlock:
  content: str


def parse_notes(lines):
  for line in lines:
    if line == '-':
      yield CardSeparator()
    elif line.startswith('#'):
      match = re.match(r'^(#+)\s*(.*)', line)
      yield Header(level=len(match.group(1)), content=match.group(2))
    else:
      content = parse_block(io.StringIO(line))
      yield Block(content=list(content))

def read_until(sio, termination_char):
  result = []

  while c := sio.read(1):
    if c == termination_char:
      return ''.join(result)
    else:
      result.append(c)
  
  raise Exception(f'Expected terminating {termination_char}')

def parse_math(sio):
  return read_until(sio, '$')

def parse_math_block(sio):
  content = read_until(sio, '$')
  if sio.read(1) == '$':
    return content
  else:
    raise Exception(f'Expected terminating $$')

def parse_block(sio):
  current = []

  while c := sio.read(1):    
    if c == '$':
      if len(current) != 0:
        yield ''.join(current)
        current = []

      c2 = sio.read(1)
      if c2 == None:
        raise Exception('Expected terminating $')
      elif c2 == '$':
        yield MathBlock(parse_math_block(sio))
      else:
        yield Math(c2 + parse_math(sio))
    else:
      current.append(c)

  yield ''.join(current)

  
lines = get_lines()
notes = list(parse_notes(lines))
for item in notes:
  print(item)
