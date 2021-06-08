import pygame
import sys
import os
 
pygame.init()
screen = pygame.display.set_mode([944, 944])
pygame.display.set_caption("Schach")
font = pygame.font.SysFont("arialblack", 50)

amZug = 1
felder = []

felder_bedroht = []

rochade_rechts_weiß = True
rochade_links_weiß = True
rochade_rechts_schwarz = True
rochade_links_schwarz = True

schach = False
figur_schach = None

feld_en_passant = None
figur_en_passant = None

farbe = (255, 0, 0)

class Feld :
    def __init__(self, x, y, farbe) :
        self.x = x
        self.y = y
        self.farbe = farbe
        self.rechteck = pygame.Rect(self.x, self.y, 118, 118)

class Figur :
    def __init__(self, x, y, bild, name, farbe, größe, nummer=1) :
        self.x = x 
        self.y = y
        self.bild = bild
        self.name = name
        self.farbe = farbe
        self.größe = größe
        self.nummer = nummer

pfad = os.path.dirname(os.path.realpath(__file__))

könig_weiß_b = pygame.image.load(pfad + "\\Bilder\\könig_weiß.png")
dame_weiß_b = pygame.image.load(pfad + "\\Bilder\\dame_weiß.png")
turm_weiß_b = pygame.image.load(pfad + "\\Bilder\\turm_weiß.png")
springer_weiß_b = pygame.image.load(pfad + "\\Bilder\\springer_weiß.png")
läufer_weiß_b = pygame.image.load(pfad + "\\Bilder\\läufer_weiß.png")
bauer_weiß_b = pygame.image.load(pfad + "\\Bilder\\bauer_weiß.png")

könig_schwarz_b = pygame.image.load(pfad + "\\Bilder\\könig_schwarz.png")
dame_schwarz_b = pygame.image.load(pfad + "\\Bilder\\dame_schwarz.png")
turm_schwarz_b = pygame.image.load(pfad + "\\Bilder\\turm_schwarz.png")
springer_schwarz_b = pygame.image.load(pfad + "\\Bilder\\springer_schwarz.png")
läufer_schwarz_b = pygame.image.load(pfad + "\\Bilder\\läufer_schwarz.png")
bauer_schwarz_b = pygame.image.load(pfad + "\\Bilder\\bauer_schwarz.png")

könig_weiß = Figur(472, 826, könig_weiß_b, "könig", "weiß", (118, 113))
dame_weiß = Figur(354, 826, dame_weiß_b, "dame", "weiß", (118, 107))
turm_weiß1 = Figur(0, 826, turm_weiß_b, "turm", "weiß", (89, 118))
turm_weiß2 = Figur(826, 826, turm_weiß_b, "turm", "weiß", (89, 118), 2)
springer_weiß1 = Figur(118, 826, springer_weiß_b, "springer", "weiß", (118, 111))
springer_weiß2 = Figur(708, 826, springer_weiß_b, "springer", "weiß", (118, 111), 2)
läufer_weiß1 = Figur(236, 826, läufer_weiß_b, "läufer", "weiß", (116, 118))
läufer_weiß2 = Figur(590, 826, läufer_weiß_b, "läufer", "weiß", (116, 118), 2)
bauer_weiß1 = Figur(0, 708, bauer_weiß_b, "bauer", "weiß", (79, 118))
bauer_weiß2 = Figur(118, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 2)
bauer_weiß3 = Figur(236, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 3)
bauer_weiß4 = Figur(354, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 4)
bauer_weiß5 = Figur(472, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 5)
bauer_weiß6 = Figur(590, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 6)
bauer_weiß7 = Figur(708, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 7)
bauer_weiß8 = Figur(826, 708, bauer_weiß_b, "bauer", "weiß", (79, 118), 8)

könig_schwarz = Figur(472, 0, könig_schwarz_b, "könig", "schwarz", (118, 114))
dame_schwarz = Figur(354, 0, dame_schwarz_b, "dame", "schwarz", (118, 106))
turm_schwarz1 = Figur(0, 0, turm_schwarz_b, "turm", "schwarz", (88, 118))
turm_schwarz2 = Figur(826, 0, turm_schwarz_b, "turm", "schwarz", (88, 118), 2)
springer_schwarz1 = Figur(118, 0, springer_schwarz_b, "springer", "schwarz", (118, 111))
springer_schwarz2 = Figur(708, 0, springer_schwarz_b, "springer", "schwarz", (118, 111), 2)
läufer_schwarz1 = Figur(236, 0, läufer_schwarz_b, "läufer", "schwarz", (115, 118))
läufer_schwarz2 = Figur(590, 0, läufer_schwarz_b, "läufer", "schwarz", (115, 118), 2)
bauer_schwarz1 = Figur(0, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118))
bauer_schwarz2 = Figur(118, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 2)
bauer_schwarz3 = Figur(236, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 3)
bauer_schwarz4 = Figur(354, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 4)
bauer_schwarz5 = Figur(472, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 5)
bauer_schwarz6 = Figur(590, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 6)
bauer_schwarz7 = Figur(708, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 7)
bauer_schwarz8 = Figur(826, 118, bauer_schwarz_b, "bauer", "schwarz", (79, 118), 8)

figuren = [könig_weiß, dame_weiß, turm_weiß1, turm_weiß2, springer_weiß1, springer_weiß2, läufer_weiß1, läufer_weiß2, bauer_weiß1, bauer_weiß2, bauer_weiß3, bauer_weiß4, bauer_weiß5, bauer_weiß6, bauer_weiß7, bauer_weiß8, könig_schwarz, dame_schwarz, turm_schwarz1, turm_schwarz2, springer_schwarz1, springer_schwarz2, läufer_schwarz1, läufer_schwarz2, bauer_schwarz1, bauer_schwarz2, bauer_schwarz3, bauer_schwarz4, bauer_schwarz5, bauer_schwarz6, bauer_schwarz7, bauer_schwarz8]

def textObjekt(text, font) :
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def zeichnen() :
    for f in figuren :
        rand = 118 - f.größe[0]
        rand2 = 118 - f.größe[1]

        screen.blit(f.bild, (f.x + rand / 2, f.y + rand2 / 2))

    pygame.display.update()

def zeichnen_felder() :
    x = 0
    y = 0
    farbe = (245, 245, 245)
    while True :
        f = Feld(x, y, farbe)
        felder.append(f)
        pygame.draw.rect(screen, farbe, (x, y, 118, 118))

        x += 118

        if x == 944 and y == 944 :
            break

        if x == 944 :
            y += 118
            x = 0
        else :
            if farbe == (245, 245, 245) :
                farbe = (139, 69, 19)
            else :
                farbe = (245, 245, 245)

    pygame.display.update()

def felder_möglich_schach(fig) :
    for figur in figuren :
        if figur.name == "könig" and figur.farbe != fig.farbe :
            for f in felder :
                if f.x == figur.x and f.y == figur.y :
                    feld = f
                    break
    
    for f in felder :
        if f.x == fig.x and f.y == fig.y :
            feld_figur = f
            break

    if fig.name == "bauer" :
        return [feld_figur]
    
    elif fig.name == "läufer" or fig.name == "dame" and feld.x != fig.x and feld.y != fig.y :
        felder2 = [feld_figur]
        if feld.x < fig.x :
            if feld.y < fig.y :
                x = fig.x - 118
                y = fig.y - 118

                while x >= 0 and y >= 0 :
                    for figur in figuren :
                        if figur.x == x and figur.y == y :
                            return felder2

                    for f in felder :
                        if f.x == x and f.y == y :
                            felder2.append(f)
                            break

                    x -= 118
                    y -= 118
            else :
                x = fig.x - 118
                y = fig.y + 118

                while x >= 0 and y < 944 :
                    for figur in figuren :
                        if figur.x == x and figur.y == y :
                            return felder2

                    for f in felder :
                        if f.x == x and f.y == y :
                            felder2.append(f)

                    x -= 118
                    y += 118

        else :
            if feld.y < fig.y :
                x = fig.x + 118
                y = fig.y - 118

                while x >= 0 and y >= 0 :
                    for figur in figuren :
                        if figur.x == x and figur.y == y :
                            return felder2

                    for f in felder :
                        if f.x == x and f.y == y :
                            felder2.append(f)

                    x += 118
                    y -= 118
            else :
                x = fig.x + 118
                y = fig.y + 118

                while x >= 0 and y < 944 :
                    for figur in figuren :
                        if figur.x == x and figur.y == y :
                            return felder2
                    
                    for f in felder :
                        if f.x == x and f.y == y :
                            felder2.append(f)

                    x += 118
                    y += 118
    
    elif fig.name == "springer" :
        return [feld_figur]

    elif fig.name == "turm" or fig.name == "dame" :
        felder2 = [feld_figur]

        if feld.x == fig.x and feld.y < fig.y :
            x = fig.x
            y = fig.y - 118

            while y >= 0 :
                for figur in figuren :
                    if figur.x == x and figur.y == y :
                        return felder2

                for f in felder :
                    if f.x == x and f.y == y :
                        felder2.append(f)
                        break
                
                y -= 118
        
        elif feld.x > fig.x and feld.y == fig.y :
            x = fig.x + 118
            y = fig.y

            while x < 944 :
                for figur in figuren :
                    if figur.x == x and figur.y == y :
                        return felder2
                
                for f in felder :
                    if f.x == x and f.y == y :
                        felder2.append(f)
                        break
                
                x += 118
        
        elif feld.x == fig.x and feld.y > fig.y :
            x = fig.x
            y = fig.y + 118

            while y < 944 :
                for figur in figuren :
                    if figur.x == x and figur.y == y :
                        return felder2
                
                for f in felder :
                    if f.x == x and f.y == y :
                        felder2.append(f)
                        break
                        
                y += 118
        
        elif feld.x < fig.x and feld.y == fig.y :
            x = fig.x - 118
            y = fig.y

            while x >= 0 :
                for figur in figuren :
                    if figur.x == x and figur.y == y :
                        return felder2
                
                for f in felder :
                    if f.x == x and f.y == y :
                        felder2.append(f)
                        break

                x -= 188


def funk_geschützt(fig, feld) :
    global farbe

    if fig.name == "bauer" :
        if fig.farbe == "weiß" :
            if feld.x == fig.x - 118 and feld.y == fig.y - 118 or feld.x == fig.x + 118 and feld.y == fig.y - 118 :
                return True
            else :
                return False
        else :
            if feld.x == fig.x - 118 and feld.y == fig.y + 118 or feld.x == fig.x + 118 and feld.y == fig.y + 118 :
                return True
            else :
                return False

    elif fig.name == "läufer" or fig.name == "dame" and feld.x != fig.x and feld.y != fig.y :
        if feld.x < fig.x :
            if feld.y < fig.y :
                x = fig.x - 118
                y = fig.y - 118

                while x >= 0 and y >= 0 :
                    if feld.x == x and feld.y == y :
                        return True

                    for figur in figuren :
                        if figur.x == x and figur.y == y and figur.name != "könig" :
                            return False

                    x -= 118
                    y -= 118
            else :
                x = fig.x - 118
                y = fig.y + 118

                while x >= 0 and y < 944 :
                    if feld.x == x and feld.y == y :
                        return True

                    for figur in figuren :
                        if figur.x == x and figur.y == y and figur.name != "könig" :
                            return False

                    x -= 118
                    y += 118

        else :
            if feld.y < fig.y :
                x = fig.x + 118
                y = fig.y - 118

                while x >= 0 and y >= 0 :
                    if feld.x == x and feld.y == y :
                        return True

                    for figur in figuren :
                        if figur.x == x and figur.y == y and figur.name != "könig" :
                            return False

                    x += 118
                    y -= 118
            else :
                x = fig.x + 118
                y = fig.y + 118

                while x >= 0 and y < 944 :
                    if feld.x == x and feld.y == y :
                        return True

                    for figur in figuren :
                        if figur.x == x and figur.y == y and figur.name != "könig" :
                            return False

                    x += 118
                    y += 118
    
    elif fig.name == "springer" :
        if feld.x == fig.x + 118 and feld.y == fig.y - 236 or feld.x == fig.x + 236 and feld.y == fig.y - 118 or feld.x == fig.x + 236 and feld.y == fig.y + 118 or feld.x == fig.x + 118 and feld.y == fig.y + 236 or feld.x == fig.x - 118 and feld.y == fig.y + 236 or feld.x == fig.x - 236 and feld.y == fig.y + 118 or feld.x == fig.x - 236 and feld.y == fig.y - 118 or feld.x == fig.x - 118 and feld.y == fig.y - 236 :
            return True
        else :
            return False
    
    elif fig.name == "turm" or fig.name == "dame" :
        if feld.x == fig.x and feld.y < fig.y :
            for figur in figuren :
                if figur.x == fig.x and figur.y < fig.y and figur.y > feld.y and figur.name != "könig" :
                    return False
            
            return True
        
        elif feld.x > fig.x and feld.y == fig.y :
            for figur in figuren :
                if figur.x > fig.x and figur.y == fig.y and figur.x < feld.x and figur.name != "könig" :
                    return False
            
            return True
        
        elif feld.x == fig.x and feld.y > fig.y :
            for figur in figuren :
                if figur.x == fig.x and figur.y > fig.y and figur.y < feld.y and figur.name != "könig" :
                    return False
            
            return True

        elif feld.x < fig.x and feld.y == fig.y :
            for figur in figuren :
                if figur.x < fig.x and figur.y == fig.y and figur.x > feld.x and figur.name != "könig" :
                    return False

            return True
        
        else :
            return False
    
    elif fig.name == "könig" :
        x = fig.x
        y = fig.y - 118

        while True :
            if x == feld.x and y == feld.y :
                return True

            if x == fig.x and y == fig.y - 118 :
                x += 118

            elif x == fig.x + 118 and y == fig.y - 118 or x == fig.x + 118 and y == fig.y :
                y += 118

            elif x == fig.x + 118 and y == fig.y + 118 or x == fig.x and y == fig.y + 118 :
                x -= 118

            elif x == fig.x - 118 and y == fig.y + 118 or x == fig.x - 118 and y == fig.y :
                y -= 118
            
            elif x == fig.x - 118 and y == fig.y - 118 :
                break
            
        return False

def felder_möglich_läufer(fig) :
    felder_möglich = []

    x = fig.x + 118
    y = fig.y - 118

    stop = False
    stop2 = False
    while x < 944 and y >= 0 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break
                
                felder_möglich.append(feld)
        
        x += 118
        y -= 118

        if stop2 :
            break

    x = fig.x + 118
    y = fig.y + 118

    stop = False
    stop2 = False
    while x < 944 and y < 944 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break
                
                felder_möglich.append(feld)
        
        x += 118
        y += 118

        if stop2 :
            break

    x = fig.x - 118
    y = fig.y + 118

    stop = False
    stop2 = False
    while x >= 0 and y < 944 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break
                
                felder_möglich.append(feld)
        
        x -= 118
        y += 118

        if stop2 :
            break

    x = fig.x - 118
    y = fig.y - 118

    stop = False
    stop2 = False
    while x >= 0 and y >= 0 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break
                
                felder_möglich.append(feld)
        
        x -= 118
        y -= 118

        if stop2 :
            break

    return felder_möglich

def felder_möglich_turm(fig) :
    felder_möglich = []

    x = fig.x
    y = fig.y - 118

    stop = False
    stop2 = False
    while y >= 0 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break

                felder_möglich.append(feld)

        if stop2 :
            break
        
        y -= 118
    
    x = fig.x + 118
    y = fig.y

    stop = False
    stop2 = False
    while x < 944 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break

                felder_möglich.append(feld)

        if stop2 :
            break
        
        x += 118
    
    x = fig.x
    y = fig.y + 118

    stop = False
    stop2 = False
    while y < 944 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break

                felder_möglich.append(feld)

        if stop2 :
            break
        
        y += 118
    
    x = fig.x - 118
    y = fig.y

    stop = False
    stop2 = False
    while x >= 0 :
        for feld in felder :
            if feld.x == x and feld.y == y :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break

                if stop :
                    stop2 = True
                    break

                felder_möglich.append(feld)

        if stop2 :
            break
        
        x -= 118

    return felder_möglich

def funk_felder_möglich(fig, f) :
    felder_möglich = []

    if fig.name == "bauer" :
        if fig.farbe == "weiß" :
            if fig.y == 708 :
                for feld in felder :
                    if feld.y == fig.y - 236 and feld.x == fig.x :
                        möglich = True
                        for figur in figuren :
                            if figur.y == fig.y - 118 and figur.x == fig.x or figur.y == fig.y - 236 and figur.x == fig.x :
                                möglich = False

                        if möglich :
                            felder_möglich.append(feld)
            
            for feld in felder :
                if feld.y == fig.y - 118 and feld.x == fig.x :
                    möglich = True
                    for figur in figuren :
                        if figur.y == fig.y - 118 and figur.x == fig.x :
                            möglich = False

                    if möglich :
                        felder_möglich.append(feld)

            for feld in felder :
                if feld.y == fig.y - 118 and feld.x == fig.x - 118 or feld.y == fig.y - 118 and feld.x == fig.x + 118 :
                    for figur in figuren :
                        if figur.x == feld.x and figur.y == feld.y and figur.farbe != fig.farbe and figur.name != "könig" :
                            felder_möglich.append(feld)
                            break
            
            if feld_en_passant != None :
                if feld_en_passant.x == fig.x - 118 and feld_en_passant.y == fig.y - 118 or feld_en_passant.x == fig.x + 118 and feld_en_passant.y == fig.y - 118 :
                    if figur_en_passant.farbe == "schwarz" :
                        felder_möglich.append(feld_en_passant)

        else :
            if fig.y == 118 :
                for feld in felder :
                    if feld.y == fig.y + 236 and feld.x == fig.x :
                        möglich = True
                        for figur in figuren :
                            if figur.y == fig.y + 118 and figur.x == fig.x or figur.y == fig.y + 236 and figur.x == fig.x :
                                möglich = False

                        if möglich :
                            felder_möglich.append(feld)
            
            for feld in felder :
                if feld.y == fig.y + 118 and feld.x == fig.x :
                    möglich = True
                    for figur in figuren :
                        if figur.y == fig.y + 118 and figur.x == fig.x :
                            möglich = False

                    if möglich :
                        felder_möglich.append(feld)

            for feld in felder :
                if feld.y == fig.y + 118 and feld.x == fig.x - 118 or feld.y == fig.y + 118 and feld.x == fig.x + 118 :
                    for figur in figuren :
                        if figur.x == feld.x and figur.y == feld.y and figur.farbe != fig.farbe and figur.name != "könig" :
                            felder_möglich.append(feld)
                            break
            
            if feld_en_passant != None :
                if feld_en_passant.x == fig.x - 118 and feld_en_passant.y == fig.y + 118 or feld_en_passant.x == fig.x + 118 and feld_en_passant.y == fig.y + 118 :
                    if figur_en_passant.farbe == "weiß" :
                        felder_möglich.append(feld_en_passant)
    
    elif fig.name == "läufer" :
        felder_möglich = felder_möglich_läufer(fig)
    
    elif fig.name == "springer" :
        stop = False
        for feld in felder :
            if feld.x == fig.x + 118 and feld.y == fig.y - 236 or feld.x == fig.x + 236 and feld.y == fig.y - 118 or feld.x == fig.x + 236 and feld.y == fig.y + 118 or feld.x == fig.x + 118 and feld.y == fig.y + 236 or feld.x == fig.x - 118 and feld.y == fig.y + 236 or feld.x == fig.x - 236 and feld.y == fig.y + 118 or feld.x == fig.x - 236 and feld.y == fig.y - 118 or feld.x == fig.x - 118 and feld.y == fig.y - 236 :
                for figur in figuren :
                    if figur.x == feld.x and figur.y == feld.y :
                        if figur.farbe == fig.farbe :
                            stop = True
                            break
                        else :
                            if figur.name != "könig" :
                                felder_möglich.append(feld)
                                stop = True
                                break
                            else :
                                stop = True
                                break
                    
                if stop :
                    stop = False
                    continue
                        
                felder_möglich.append(feld)
    
    elif fig.name == "turm" :
        felder_möglich = felder_möglich_turm(fig)
    
    elif fig.name == "dame" :
        felder_möglich = felder_möglich_turm(fig) + felder_möglich_läufer(fig)
    
    elif fig.name == "könig" :
        if fig.farbe == "weiß" :
            möglich = True
            if rochade_links_weiß :
                for figur in figuren :
                    if figur.x == felder[57].x and figur.y == 826 or figur.x == felder[58].x and figur.y == 826 or figur.x == felder[59].x and figur.y == 826 :
                        möglich = False
                        break

                    if figur.farbe == "schwarz" :
                        if funk_geschützt(figur, felder[58]) or funk_geschützt(figur, felder[59]) or funk_geschützt(figur, felder[60]) :
                            möglich = False
                            break
                
                if möglich :
                    felder_möglich.append(felder[58])
            
            möglich = True
            if rochade_rechts_weiß :
                for figur in figuren :
                    if figur.x == felder[61].x and figur.y == 826 or figur.x == felder[62].x and figur.y == 826 :
                        möglich = False
                        break

                    if figur.farbe == "schwarz" :
                        if funk_geschützt(figur, felder[61]) or funk_geschützt(figur, felder[62]) :
                            möglich = False
                            break
                
                if möglich :
                    felder_möglich.append(felder[62])
        
        else :
            möglich = True
            if rochade_links_schwarz :
                for figur in figuren :
                    if figur.x == felder[1].x and figur.y == 0 or figur.x == felder[2] and figur.y == 0 or figur.x == felder[3].x and figur.y == 0 :
                        möglich = False
                        break

                    if figur.farbe == "weiß" :
                        if funk_geschützt(figur, felder[2]) or funk_geschützt(figur, felder[3]) or funk_geschützt(figur, felder[4]) :
                            möglich = False
                            break
                
                if möglich :
                    felder_möglich.append(felder[2])
            
            möglich = True
            if rochade_rechts_schwarz :
                for figur in figuren :
                    if figur.x == felder[5].x and figur.y == 0 or figur.x == felder[6].x and figur.y == 0 :
                        möglich = False
                        break

                    if figur.farbe == "weiß" :
                        if funk_geschützt(figur, felder[4]) or funk_geschützt(figur, felder[5]) or funk_geschützt(figur, felder[6]) :
                            möglich = False
                            break
                
                if möglich :
                    felder_möglich.append(felder[6])

        x = fig.x
        y = fig.y - 118

        while True :
            stop = False
            for feld in felder :
                if feld.x == x and feld.y == y :
                    for figur in figuren :
                        if figur.farbe != fig.farbe :
                            if funk_geschützt(figur, feld) :
                                stop = True
                                break

                        if figur.x == feld.x and figur.y == feld.y :
                            if figur.farbe == fig.farbe :
                                stop = True
                                break
                            else :
                                if figur.name == "könig" :
                                    stop = True
                                    break
                                else :
                                    felder_möglich.append(feld)
                                    stop = True
                                    break
                    
                    if stop :
                        break

                    felder_möglich.append(feld)
            
            if x == fig.x and y == fig.y - 118 :
                x += 118

            elif x == fig.x + 118 and y == fig.y - 118 or x == fig.x + 118 and y == fig.y :
                y += 118

            elif x == fig.x + 118 and y == fig.y + 118 or x == fig.x and y == fig.y + 118 :
                x -= 118

            elif x == fig.x - 118 and y == fig.y + 118 or x == fig.x - 118 and y == fig.y :
                y -= 118
            
            elif x == fig.x - 118 and y == fig.y - 118 :
                break

    stop = False
    for figur in figuren :
        if figur.name == "könig" and figur.farbe == fig.farbe :
            if figur.x == fig.x and figur.y < fig.y :
                for figur2 in figuren :
                    if figur2.x == figur.x and figur2.y < fig.y and figur2.y > figur.y :
                        stop = True
                        break
                
                if not stop :
                    for figur2 in figuren :
                        if figur2.name == "turm" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            if figur2.x == fig.x and figur2.y > fig.y :
                                if funk_geschützt(figur2, f) :
                                    i = 0
                                    while i < len(felder_möglich) :
                                        entfernen = True
                                        if felder_möglich[i].x == figur.x and felder_möglich[i].y > fig.y and felder_möglich[i].y <= figur2.y :
                                            entfernen = False

                                        if entfernen :
                                            felder_möglich.remove(felder_möglich[i])
                                        else :
                                            i += 1
            
            elif figur.x > fig.x and figur.y == fig.y :
                for figur2 in figuren :
                    if figur2.x < figur.x and figur2.x > fig.x and figur2.y == fig.y :
                        stop = True
                        break
                
                if not stop :
                    for figur2 in figuren :
                        if figur2.name == "turm" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            if figur2.x < fig.x and figur2.y == fig.y :
                                if funk_geschützt(figur2, f) :
                                    i = 0
                                    while i < len(felder_möglich) :
                                        entfernen = True
                                        if felder_möglich[i].x < figur.x and felder_möglich[i].x >= figur2.x and felder_möglich[i].y == fig.y :
                                            entfernen = False

                                        if entfernen :
                                            felder_möglich.remove(felder_möglich[i])
                                        else :
                                            i += 1
            
            elif figur.x == fig.x and figur.y > fig.y :
                for figur2 in figuren :
                    if figur2.x == figur.x and figur2.y < figur.y and figur2.y > fig.y :
                        stop = True
                        break
                
                if not stop :
                    for figur2 in figuren :
                        if figur2.name == "turm" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            if figur2.x == fig.x and figur2.y < fig.y :
                                if funk_geschützt(figur2, f) :
                                    i = 0
                                    while i < len(felder_möglich) :
                                        entfernen = True
                                        if felder_möglich[i].x == figur.x and felder_möglich[i].y < fig.y and felder_möglich[i].y >= figur2.y :
                                            entfernen = False

                                        if entfernen :
                                            felder_möglich.remove(felder_möglich[i])
                                        else :
                                            i += 1
            
            elif figur.x < fig.x and figur.y == fig.y :
                for figur2 in figuren :
                    if figur2.x > figur.x and figur2.x < fig.x and figur2.y == fig.y :
                        stop = True
                        break
                
                if not stop :
                    for figur2 in figuren :
                        if figur2.name == "turm" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            if figur2.x > fig.x and figur2.y == fig.y :
                                if funk_geschützt(figur2, f) :
                                    i = 0
                                    while i < len(felder_möglich) :
                                        entfernen = True
                                        if felder_möglich[i].x > figur.x and felder_möglich[i].x <= figur2.x and felder_möglich[i].y == fig.y :
                                            entfernen = False

                                        if entfernen :
                                            felder_möglich.remove(felder_möglich[i])
                                        else :
                                            i += 1

            entfernung_x = figur.x - fig.x
            entfernung_y = figur.y - fig.y

            if entfernung_x < 0 :
                entfernung_x *= -1

            if entfernung_y < 0 :
                entfernung_y *= -1

            if entfernung_x == entfernung_y :
                if figur.x > fig.x and figur.y < fig.y :
                    for figur2 in figuren :
                        if figur2.name == "läufer" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            entfernung_x2 = figur2.x - fig.x
                            entfernung_y2 = figur2.y - fig.y

                            if entfernung_x2 < 0 :
                                entfernung_x2 *= -1

                            if entfernung_y2 < 0 :
                                entfernung_y2 *= -1

                            if figur2.x < fig.x and figur2.y > fig.y and entfernung_x2 == entfernung_y2 :
                                felder_möglich2 = []

                                x = fig.x - 118
                                y = fig.y + 118
                                while x >= figur2.x and y <= figur2.y :
                                    for figur in figuren :
                                        if figur.x == x and figur.y == y :
                                            break

                                    for feld in felder :
                                        if feld.x == x and feld.y == y :
                                            felder_möglich2.append(feld)
                                    
                                    x -= 118
                                    y += 118
                                
                                i = 0 
                                while i < len(felder_möglich) :
                                    if not felder_möglich[i] in felder_möglich2 :
                                        felder_möglich.remove(felder_möglich[i])
                                    else :
                                        i += 1 
                    
                elif figur.x > fig.x and figur.y > fig.y :
                    for figur2 in figuren :
                        if figur2.name == "läufer" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            entfernung_x2 = figur2.x - fig.x
                            entfernung_y2 = figur2.y - fig.y

                            if entfernung_x2 < 0 :
                                entfernung_x2 *= -1

                            if entfernung_y2 < 0 :
                                entfernung_y2 *= -1

                            if figur2.x < fig.x and figur2.y < fig.y and entfernung_x2 == entfernung_y2 :
                                felder_möglich2 = []

                                x = fig.x - 118
                                y = fig.y - 118
                                while x >= figur2.x and y >= figur2.y :
                                    for figur in figuren :
                                        if figur.x == x and figur.y == y :
                                            break

                                    for feld in felder :
                                        if feld.x == x and feld.y == y :
                                            felder_möglich2.append(feld)
                                    
                                    x -= 118
                                    y -= 118
                                
                                i = 0 
                                while i < len(felder_möglich) :
                                    if not felder_möglich[i] in felder_möglich2 :
                                        felder_möglich.remove(felder_möglich[i])
                                    else :
                                        i += 1 
                
                elif figur.x < fig.x and figur.y > fig.y :
                    for figur2 in figuren :
                        if figur2.name == "läufer" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            entfernung_x2 = figur2.x - fig.x
                            entfernung_y2 = figur2.y - fig.y

                            if entfernung_x2 < 0 :
                                entfernung_x2 *= -1

                            if entfernung_y2 < 0 :
                                entfernung_y2 *= -1

                            if figur2.x > fig.x and figur2.y < fig.y and entfernung_x2 == entfernung_y2 :
                                felder_möglich2 = []

                                x = fig.x + 118
                                y = fig.y - 118
                                while x <= figur2.x and y >= figur2.y :
                                    for figur in figuren :
                                        if figur.x == x and figur.y == y :
                                            break

                                    for feld in felder :
                                        if feld.x == x and feld.y == y :
                                            felder_möglich2.append(feld)
                                    
                                    x += 118
                                    y -= 118
                                
                                i = 0 
                                while i < len(felder_möglich) :
                                    if not felder_möglich[i] in felder_möglich2 :
                                        felder_möglich.remove(felder_möglich[i])
                                    else :
                                        i += 1 
                
                elif figur.x < fig.x and figur.y < fig.y :
                    for figur2 in figuren :
                        if figur2.name == "läufer" and figur2.farbe != fig.farbe or figur2.name == "dame" and figur2.farbe != fig.farbe :
                            entfernung_x2 = figur2.x - fig.x
                            entfernung_y2 = figur2.y - fig.y

                            if entfernung_x2 < 0 :
                                entfernung_x2 *= -1

                            if entfernung_y2 < 0 :
                                entfernung_y2 *= -1

                            if figur2.x > fig.x and figur2.y > fig.y and entfernung_x2 == entfernung_y2 :
                                felder_möglich2 = []

                                x = fig.x + 118
                                y = fig.y + 118
                                while x <= figur2.x and y <= figur2.y :
                                    for figur in figuren :
                                        if figur.x == x and figur.y == y :
                                            break

                                    for feld in felder :
                                        if feld.x == x and feld.y == y :
                                            felder_möglich2.append(feld)
                                    
                                    x += 118
                                    y += 118
                                
                                i = 0 
                                while i < len(felder_möglich) :
                                    if not felder_möglich[i] in felder_möglich2 :
                                        felder_möglich.remove(felder_möglich[i])
                                    else :
                                        i += 1 

    return felder_möglich

def verwandeln(fig) :
    zeichnen_felder()
    zeichnen()

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT: sys.exit()

        pygame.draw.rect(screen, (150, 50, 50), (236, 413, 472, 118))

        pos = pygame.mouse.get_pos()

        if pos[0] > 236 and pos[0] < 354 and pos[1] > 413 and pos[1] < 531 :
            pygame.draw.rect(screen, (200, 50, 50), (236, 413, 118, 118))

        elif pos[0] > 354 and pos[0] < 472 and pos[1] > 413 and pos[1] < 531 :
            pygame.draw.rect(screen, (200, 50, 50), (351, 413, 118, 118))

        elif pos[0] > 472 and pos[0] < 590 and pos[1] > 413 and pos[1] < 531 :
            pygame.draw.rect(screen, (200, 50, 50), (472, 413, 118, 118))

        elif pos[0] > 590 and pos[0] < 708 and pos[1] > 413 and pos[1] < 531 :
            pygame.draw.rect(screen, (200, 50, 50), (590, 413, 118, 118))

        if fig.farbe == "weiß" :
            screen.blit(dame_weiß_b, (236, 413))
            screen.blit(turm_weiß_b, (368.5, 413))
            screen.blit(springer_weiß_b, (472, 413))
            screen.blit(läufer_weiß_b, (590, 413))

        else :
            screen.blit(dame_schwarz_b, (236, 413))
            screen.blit(turm_schwarz_b, (368.5, 413))
            screen.blit(springer_schwarz_b, (472, 413))
            screen.blit(läufer_schwarz_b, (590, 413))
        
        pygame.display.update()

        maus = pygame.mouse.get_pressed()

        if maus[0] :
            pos = pygame.mouse.get_pos()

            if pos[0] > 236 and pos[0] < 354 and pos[1] > 413 and pos[1] < 531 :
                if fig.farbe == "weiß" :
                    figur_neu = Figur(fig.x, fig.y, dame_weiß_b, "dame", "weiß", (118, 107))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu
                else :
                    figur_neu = Figur(fig.x, fig.y, dame_schwarz_b, "dame", "schwarz", (118, 106))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu
            
            elif pos[0] > 354 and pos[0] < 472 and pos[1] > 413 and pos[1] < 531 :
                if fig.farbe == "weiß" :
                    figur_neu = Figur(fig.x, fig.y, turm_weiß_b, "turm", "weiß", (89, 118))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu
                else :
                    figur_neu = Figur(fig.x, fig.y, turm_schwarz_b, "turm", "schwaz", (88, 118))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu

            elif pos[0] > 472 and pos[0] < 590 and pos[1] > 413 and pos[1] < 531 :
                if fig.farbe == "weiß" :
                    figur_neu = Figur(fig.x, fig.y, springer_weiß_b, "springer", "weiß", (118, 111))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu
                else :
                    figur_neu = Figur(fig.x, fig.y, springer_schwarz_b, "springer", "schwarz", (118, 111))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu

            elif pos[0] > 590 and pos[0] < 708 and pos[1] > 413 and pos[1] < 531 :
                if fig.farbe == "weiß" :
                    figur_neu = Figur(fig.x, fig.y, läufer_weiß_b, "läufer", "weiß", (116, 118))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu
                else :
                    figur_neu = Figur(fig.x, fig.y, läufer_schwarz_b, "läufer", "schwarz", (115, 118))
                    figuren.remove(fig)
                    figuren.append(figur_neu)
                    return figur_neu

def ziehen(pos) :
    global amZug
    global rochade_rechts_weiß, rochade_links_weiß, rochade_rechts_schwarz, rochade_links_schwarz
    global feld_en_passant, figur_en_passant
    global schach, figur_schach

    stop = False
    stop2 = False

    for f in felder :
        if f.rechteck.colliderect(pygame.Rect(pos[0], pos[1], 1, 1)) :
            for fig in figuren :
                if fig.x == f.x and fig.y == f.y :
                    if amZug == 1 and fig.farbe == "schwarz" :
                        stop = True
                        break
                    elif amZug == 2 and fig.farbe == "weiß" :
                        stop= True
                        break

                    f.rechteck = pygame.draw.rect(screen, (255, 255, 0), (f.x, f.y, 118, 118))
                    zeichnen()
                    ende = False

                    pygame.time.wait(500)

                    felder_möglich = funk_felder_möglich(fig, f)
                    
                    if schach and fig.name != "könig" :
                        felder_möglich2 = felder_möglich_schach(figur_schach)

                        i = 0
                        while i < len(felder_möglich) :
                            feld = felder_möglich[i]

                            if not feld in felder_möglich2 :
                                felder_möglich.remove(felder_möglich[i])
                            else :
                                i += 1

                    for f in felder_möglich :
                        pygame.draw.circle(screen, (0, 255, 0), (f.x + 59, f.y + 59), 15)
                    
                    pygame.display.update()

                    while True :
                        for event in pygame.event.get() :
                            if event.type == pygame.QUIT: sys.exit()

                        maus = pygame.mouse.get_pressed()
                        
                        if maus[0] :
                            for f2 in felder :
                                pos2 = pygame.mouse.get_pos()
                                if f2.rechteck.colliderect(pygame.Rect(pos2[0], pos2[1], 1, 1)) and f2 in felder_möglich :
                                    frei = True
                                    schach = False
                                    for figur in figuren :
                                        if figur.x == f2.x and figur.y == f2.y :
                                            frei = False

                                            if figur.farbe != fig.farbe and figur.name != "könig" :
                                                if fig.name == "turm" :
                                                    if fig.farbe == "weiß" :
                                                        if fig.nummer == 1 :
                                                            rochade_links_weiß = False
                                                        else :
                                                            rochade_rechts_weiß = False
                                                    else :
                                                        if fig.nummer == 1 :
                                                            rochade_links_schwarz = False
                                                        else :
                                                            rochade_rechts_schwarz = False

                                                elif fig.name == "könig" :
                                                    if fig.farbe == "weiß" :
                                                        rochade_links_weiß = False
                                                        rochade_rechts_weiß = False
                                                    else :
                                                        rochade_links_schwarz = False
                                                        rochade_rechts_schwarz = False

                                                figuren.remove(figur)
                                                fig.x = f2.x 
                                                fig.y = f2.y
                                                ende = True

                                                if fig.name == "bauer" and fig.y == 0 or fig.name == "bauer" and fig.y == 826 :
                                                    fig = verwandeln(fig)
                                                
                                                if amZug == 1 :
                                                    amZug = 2
                                                else :
                                                    amZug = 1

                                                pygame.time.wait(500)
                                                break
                                    
                                    if frei :
                                        if fig.name == "turm" :
                                            if fig.farbe == "weiß" :
                                                if fig.nummer == 1 :
                                                    rochade_links_weiß = False
                                                else :
                                                    rochade_rechts_weiß = False
                                            else :
                                                if fig.nummer == 1 :
                                                    rochade_links_schwarz = False
                                                else :
                                                    rochade_rechts_schwarz = False

                                        elif fig.name == "könig" :
                                            if fig.farbe == "weiß" :
                                                if f2.x == felder[58].x and f2.y == felder[58].y :
                                                    for figur in figuren :
                                                        if figur.name == "turm" and figur.farbe == "weiß" and figur.nummer == 1 :
                                                            figur.x = felder[59].x
                                                            figur.y = felder[59].y

                                                elif f2.x == felder[62].x and f2.y == felder[62].y :
                                                    for figur in figuren :
                                                        if figur.name == "turm" and figur.farbe == "weiß" and figur.nummer == 2 :
                                                            figur.x = felder[61].x
                                                            figur.y = felder[61].y

                                                rochade_links_weiß = False
                                                rochade_rechts_weiß = False
                                            else :
                                                if f2.x == felder[2].x and f2.y == 0 :
                                                    for figur in figuren :
                                                        if figur.name == "turm" and figur.farbe == "schwarz" and figur.nummer == 1 :
                                                            figur.x = felder[3].x
                                                            figur.y = felder[3].y

                                                elif f2.x == felder[6].x and f2.y == 0 :
                                                    for figur in figuren :
                                                        if figur.name == "turm" and figur.farbe == "schwarz" and figur.nummer == 2 :
                                                            figur.x = felder[5].x
                                                            figur.y = felder[5].y

                                                rochade_links_schwarz = False
                                                rochade_rechts_schwarz = False
                                        
                                        elif fig.name == "bauer" :
                                            if f2 == feld_en_passant :
                                                figuren.remove(figur_en_passant)

                                            if fig.farbe ==  "weiß" :
                                                if f2.x == fig.x and f2.y == fig.y - 236 :
                                                    for feld in felder :
                                                        if feld.x == fig.x and feld.y == fig.y - 118 :
                                                            feld_en_passant = feld
                                                            figur_en_passant = fig
                                                            break
                                                else :
                                                    feld_en_passant = None
                                                    figur_en_passant = None
                                                
                                            else :
                                                if f2.x == fig.x and f2.y == fig.y + 236 :
                                                    for feld in felder :
                                                        if feld.x == fig.x and feld.y == fig.y + 118 :
                                                            feld_en_passant = feld
                                                            figur_en_passant = fig
                                                            break
                                                else :
                                                    feld_en_passant = None
                                                    figur_en_assant = None

                                        fig.x = f2.x 
                                        fig.y = f2.y
                                        ende = True

                                        if fig.name == "bauer" and fig.y == 0 or fig.name == "bauer" and fig.y == 826 :
                                            fig = verwandeln(fig)

                                        if amZug == 1 :
                                            amZug = 2
                                        else :
                                            amZug = 1

                                        pygame.time.wait(500)
                                        break
                            
                            for figur in figuren :
                                if figur.name == "könig" and figur.farbe != fig.farbe :
                                    for feld in felder :
                                        if feld.x == figur.x and feld.y == figur.y :
                                            if funk_geschützt(fig, feld) :
                                                schach = True
                                                figur_schach = fig

                                                matt = True
                                                for figur2 in figuren :
                                                    if figur2.farbe != figur_schach.farbe :
                                                        if figur2.name != "könig" :
                                                            for feld in felder :
                                                                if feld.x == figur2.x and feld.y == figur2.y :
                                                                    felder_möglich2 = felder_möglich_schach(figur_schach)
                                                                    felder_möglich = funk_felder_möglich(figur2, feld)
                                                                    break

                                                            i = 0 
                                                            while i < len(felder_möglich) :
                                                                if not felder_möglich[i] in felder_möglich2 :
                                                                    felder_möglich.remove(felder_möglich[i])
                                                                else :
                                                                    i += 1 

                                                            if len(felder_möglich) > 0 :
                                                                matt = False
                                                                break
                                                        else :
                                                            for feld in felder :
                                                                if feld.x == figur2.x and feld.y == figur2.y :
                                                                    if len(funk_felder_möglich(figur2, feld)) > 0 :
                                                                        matt = False
                                                                        break
                                                        
                                                if matt :
                                                    zeichnen_felder()
                                                    zeichnen()

                                                    if fig.farbe == "weiß" :
                                                        textGrund,textKasten = textObjekt("Weiß hat gewonnen!", font)
                                                    else :
                                                        textGrund,textKasten = textObjekt("Schwarz hat gewonnen!", font)

                                                    textKasten.center = ((472, 472))
                                                    screen.blit(textGrund,textKasten)
                                                    pygame.display.update()

                                                    ende = False

                                                    while True :
                                                        for event in pygame.event.get() :
                                                            if event.type == pygame.QUIT: sys.exit()
                                                        
                                                        gedrueckt = pygame.key.get_pressed()

                                                        for k in gedrueckt :
                                                            if k :
                                                                if ende :
                                                                    sys.exit()
                                                                else :
                                                                    ende = True
                                                                    zeichnen_felder()
                                                                    zeichnen()
                                                                    pygame.display.update()
                                                                    pygame.time.wait(500)

                        elif maus[2] or ende :
                            stop = True
                            break

                if stop :
                    stop2 = True
                    break

        if stop2 :
            break

    zeichnen_felder()
    zeichnen()

zeichnen_felder()

go = True
while go :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: sys.exit()

    maus = pygame.mouse.get_pressed()

    if maus[0] :
        ziehen(pygame.mouse.get_pos())

    zeichnen()