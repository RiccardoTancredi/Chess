from pylatex import Document
from pylatex.base_classes import Environment, Command, Container, LatexObject, \
    UnsafeCommand
from pylatex.utils import italic, NoEscape
import os
from pylatex.package import Package

class Chess(Environment):
    """A class to wrap LaTeX's alltt environment."""

    packages = [Package('skak')]
    escape = False
    content_separator = "\n"



def latex_init():
    # with open(file_name, 'w') as file:
    #     file.write("\\documentclass{article}\n")
    #     file.write("\\usepackage[utf8]{inputenc}\n")
    #     file.write("\\usepackage[english]{babel}\n")
    #     file.write("\\usepackage{skak}\n")
    #     file.write("\\begin{document}\n")
    #     file.write("\\newgame\n")
    #     file.write("\\showboard\n")
    doc = Document()
    with doc.create(Chess()):
        start = ("\\newgame\n"
                    "\\showboard\n"
                    # "\\mainline{1.e4 e5}"
                    )
        doc.append(start)
    return doc

def latex_write(doc, chess_notation):
    # with open(file_name, 'a') as file:
    #     file.write("\\mainline{")
    #     file.write(chess_notation)
    #     file.write("}\n")
    #     file.write("\\showboard\n")

    moves = "\\mainline{" + chess_notation + "}\n" + "\\showboard\n"
    with doc.create(Chess()):
        boards = (moves)
        doc.append(boards)
        return doc

# def latex_end(doc):
#     with open(file_name, 'a') as file:
#         file.write("\\end{document}\n")

def convert_to_PDF(doc, name):
    doc.generate_pdf(name, compiler='pdfLaTeX')