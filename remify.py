import sublime, sublime_plugin, re

settings = sublime.load_settings("Remify.sublime-settings")

class Remify(sublime_plugin.TextCommand):
  def run(self, edit):
    sels = self.view.sel()
    output = ""

    for sel in sels:
      sel = self.view.line(sel)
      lines = self.view.substr(sel).split("\n")

      for i, line in enumerate(lines):
        output = RemifyTools.convert(line)

    self.view.replace(edit, sel, output)

  def get_line_num(self, point):
    return self.view.rowcol(point)[0] + 1

class RemifyTools:
  @classmethod
  def convert(self, selection):
    # margin: $baseline-small $gutter-half 0 $gutter-half
    # margin-bottom: 5px
    # border: 1px solid #000
    # padding: 0px 0px 5px 5px
    # border-radius: $border-radius-base
    # box-shadow: inset 0 0 6px rgba($black, .16)

    selector = selection.split(":")

    attr = selector[0]
    prop = selector[1]

    whitespace = attr.split(" ")
    attribute = whitespace.pop()
    indent = ""

    for space in whitespace:
      indent += " "

    result = indent + "+rem(" + attribute + ", " + prop.strip() + ")"

    return result
