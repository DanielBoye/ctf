#!/usr/bin/env python3

class Emojifier(dict):
    def __init__(self):
        self.art = ['🐄','🥛','🐮','🚩']
    def __getitem__(self, key):
        return self.art[key]

def main(locals):
  print()
  print("""
           +--------------+
          /|             /|
         / |            / |
        *--+-----------*  |
        |  |           |  |
        |  |           |  |
        |  |   moo?    |  |
        |  +-----------+--+
        | /            | /
        |/             |/
        *--------------*
  """)
  print()
  
  blacklist = "()"
  
  while True:
      inp = input('> ')
      if any(x in inp for x in blacklist):
        print(":moo:")
        exit()
  
      co = compile(inp, "jail", "eval")
      res = eval(co, {'__builtins__': {"art": Emojifier(), ":)": __import__}}, locals)
      locals["_"] = res
      print(repr(res))

locals = {}
if __name__ == '__main__':
  main(locals)
