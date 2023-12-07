import win32gui
import win32api

dc = win32gui.GetDC(0)

class color:

    white = win32api.RGB(255, 255, 255)
    black = win32api.RGB(0, 0, 0)
    red = win32api.RGB(255, 0, 0)
    green = win32api.RGB(0, 255, 0)
    blue = win32api.RGB(0, 0, 255)


class draw:

    def pixel(x,y,color):
        win32gui.SetPixel(dc, x, y, color)

    def line(x1, y1, x2, y2, color):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while True:
            draw.pixel(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def box(x1, y1, x2, y2, color):
        draw.line(x1, y1, x2, y1, color)
        draw.line(x1, y1, x1, y2, color)
        draw.line(x2, y1, x2, y2, color)
        draw.line(x1, y2, x2, y2, color)

    class dropshadow:

        def box(x1, y1, x2, y2, color, color_shadow):

            x1_shadow1 = x1 + 1
            y1_shadow1 = y1 + 1
            x2_shadow1 = x2 + 1
            y2_shadow1 = y2 + 1

            x1_shadow2 = x1 + 2
            y1_shadow2 = y1 + 2
            x2_shadow2 = x2 + 2
            y2_shadow2 = y2 + 2

            draw.box(x1_shadow1, y1_shadow1, x2_shadow1, y2_shadow1, color_shadow)
            draw.box(x1_shadow2, y1_shadow2, x2_shadow2, y2_shadow2, color_shadow)
            draw.box(x1, y1, x2, y2, color)

    class outlined:
        
        def box(x1, y1, x2, y2, color, color_outline):

            draw.box(x1, y1, x2, y2, color)
            draw.box(x1 - 1, y1 - 1, x2 - 1, y2 - 1, color_outline)
            draw.box(x1 + 1, y1 + 1, x2 + 1, y2 + 1, color_outline)



def main():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    print('dropshadow')
    while counter1 < 250:
        draw.dropshadow.box(100, 100, 300, 500, color.red, color.black)
        counter1 += 1
    print('outlined')
    while counter2 < 250:
        draw.outlined.box(100, 100, 300, 500, color.red, color.black)
        counter2 += 1
    print('normal')
    while counter3 < 250:
        draw.box(100, 100, 300, 500, color.red)
        counter3 += 1

if __name__ == "__main__":       
    while True:
        main()