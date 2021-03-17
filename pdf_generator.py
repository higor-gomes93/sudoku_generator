from fpdf import FPDF
import sudoku_generator
import image_croper

total_sudokus = sudoku_generator.total_sudokus

difficiult = sudoku_generator.difficiult

# Checando o valor da dificuldade
if difficiult >= 5:
    nivel = "Difícil"
elif 3 <= difficiult < 5:
    nivel = "Médio"
else:
    nivel = "Fácil"

# Criando a classe para geração do PDF
class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.5)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one
    pass

pdf = PDF()

# Capa
pdf.add_page()
pdf.set_auto_page_break(False, margin=0)
pdf.set_xy(0, 0)
pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/Sudoku/capa.png', w = 210, h = 297, type = 'PNG')
pdf.set_font('Arial', 'B', 14)
pdf.set_y(240)
pdf.cell(0, 0, 'Nível: '+nivel, 0, 0, 'C')

# Descobrindo o total de páginas
if total_sudokus%2 == 0:
    total = int(total_sudokus/2)
else:
    total = total_sudokus//2 + 1

# Escrevendo os jogos
for i in range(total):
    pdf.add_page()
    pdf.lines()
    pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/sudoku'+str(1+2*i)+'.png', x = 45, y = 18, type='PNG')
    if 2+2*i <= total_sudokus:
        pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/sudoku'+str(2+2*i)+'.png', x = 45, y = 153, type='PNG')
    pdf.set_font('Arial', 'B', 14)
    pdf.set_y(285)
    pdf.set_auto_page_break(False, margin=0)
    pdf.cell(0, 0, str(i+1), 0, 0, 'C')

# Fazendo a capa de Respostas
pdf.add_page()
pdf.set_auto_page_break(False, margin=0)
pdf.set_xy(0, 0)
pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/Sudoku/respostas.png', w = 210, h = 297, type = 'PNG')

# Escrevendo as respostas
for i in range(total):
    pdf.add_page()
    pdf.lines()
    pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/resolucao'+str(1+2*i)+'.png', x = 45, y = 18, type='PNG')
    if 2+2*i <= total_sudokus:
        pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/resolucao'+str(2+2*i)+'.png', x = 45, y = 153, type='PNG')
    pdf.set_font('Arial', 'B', 14)
    pdf.set_y(285)
    pdf.set_auto_page_break(False, margin=0)
    pdf.cell(0, 0, str(i+1), 0, 0, 'C')

# Fazendo a contracapa
pdf.add_page()
pdf.set_auto_page_break(False, margin=0)
pdf.set_xy(0, 0)
pdf.image('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/Sudoku/contracapa.png', w = 210, h = 297, type = 'PNG')

# Imprimindo o PDF
pdf.output('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/Sudoku/sudoku.pdf', 'F')