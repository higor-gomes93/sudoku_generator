import numpy as np
from PIL import Image

total_sudokus = 4

def bbox(im):
    a = np.array(im)[:,:,:3]
    m = np.any(a != [255, 255, 255], axis=2)
    coords = np.argwhere(m)
    y0, x0, y1, x1 = *np.min(coords, axis=0), *np.max(coords, axis=0)
    return (x0, y0, x1+1, y1+1)

for i in range(total_sudokus):
    im_sudoku = Image.open('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/sudoku'+str(i+1)+'.png')
    im_sudoku_cropped = im_sudoku.crop(bbox(im_sudoku))
    im_sudoku_cropped.save('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/sudoku'+str(i+1)+'.png')
    
    im_resolucao = Image.open('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/resolucao'+str(i+1)+'.png')
    im_resolucao_cropped = im_resolucao.crop(bbox(im_resolucao))
    im_resolucao_cropped.save('c:/Users/Usuario/Documents/Estudos/Programação/Algoritmos/resolucao'+str(i+1)+'.png')