# Feihong's Anki Quickstart

## Installation

Download [Anki](https://apps.ankiweb.net/), open .dmg file, drag into Applications.

Install Python and run

    pip install --requirement requirements.txt

## Commands

Create a new app in your `~/Applications` that runs Anki but uses its own
separate user data folder.

    make anki

## Notes

It's possible to import cards containing MathJax (TeX). See `exported.txt` for an example.

You must replace any instances of consecutive braces (e.g. `}}`) with brace+space (e.g. `} } `) so as to not conflict with the Cloze delimiter `}}`. See [Cloze Conflicts section](https://docs.ankiweb.net/math.html#cloze-conflicts) of Anki Manual.

Anki tags cannot contain spaces. They can contain underscores, though.

Anki doesn't allow cloze deletions inside MathJax elements.

## Links

- [AsciiMath syntax](http://asciimath.org/#syntax)
- [Anki Manual: Math & Symbols](https://docs.ankiweb.net/math.html)
- [Anki Manual: File Headers](https://docs.ankiweb.net/importing.html#file-headers)
- [How to make Mac app with shell
  script](https://apple.stackexchange.com/a/269045)
