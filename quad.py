'''
Takes a, b, c as inputs and returns an dictionary containing the keys 
'eqn' (equation), 'nature' (nature of the equation), 'dsc' (the discriminant), 'roots' (roots of the equation if present)
NOTE: If roots are not available, then an empty string ('') will be issued as the value
'''

class Cal():

    def __init__(self, a, b, c):
        self.a1 = a
        self.b1 = b
        self.c1 = c
        self.output_label = {}

    def proceedure(self):
        discriminant = self.discriminant
        a = self.a
        b = self.b
        c = self.c
        if discriminant > 0:
            import math
            root_discriminant = math.sqrt(discriminant)
            x1 = (-b + root_discriminant)/(2*a)
            x2 = (-b - root_discriminant)/(2*a)
            rts = f"\nx\u2081 = {x1} \nx\u2082 = {x2}"
            say = f"roots of the equation are: {rts}"

        elif discriminant == 0:
            import math
            root_discriminant = math.sqrt(discriminant)
            x = -b/2
            rts = f"x = {x}"
            say = f"your coincident root is: {rts}"

        if discriminant >= 0:
            return say

    def nature(self):

        discriminant = self.discriminant
        a = self.a

        if discriminant > 0:
            nat = 'The equation has 2 distinct real roots'

        elif discriminant == 0:
            nat = 'The equation has one real coincident root'

        if discriminant < 0 and a > 0:
            nat = 'The equation has no real roots and is always positive'

        elif discriminant < 0 and a < 0:
            nat = 'The equation has no real roots and is always negative'

        return nat

    def equation(self):
        a1 = self.a1
        b1 = self.b1
        c1 = self.c1
        a = self.a
        b = self.b
        c = self.c
        l = a1.rstrip('0').rstrip('.') if '.' in a1 else a1
        m = b1.rstrip('0').rstrip('.') if '.' in b1 else b1
        n = c1.rstrip('0').rstrip('.') if '.' in c1 else c1

        if a == 1:
            l = ""

        elif a == -1:
            l = "-"

        if b == 1:
            m = ""

        elif b == -1:
            m = "-"

        if b < 0:
            if c < 0:
                eq = f"your equation is:  y={l}x\u00b2{m}x{n}"

            else:
                eq = f"your equation is:  y={l}x\u00b2{m}x+{n}"

        elif c < 0:
            eq = f"your equation is:  y={l}x\u00b2+{m}x{n}"

        else:
            eq = f"your equation is: y={l}x\u00b2+{m}x+{n}"

        return eq

    def error_handeling(self):
        output_label = self.output_label
        try:
            self.a = eval(self.a1)
            self.b = eval(self.b1)
            self.c = eval(self.c1)

        except (NameError, SyntaxError):
            raise ValueError

        if self.a == 0:
            raise ValueError

    def run(self):
        self.error_handeling()
        a = self.a
        b = self.b
        c = self.c
        out = self.output_label
        self.discriminant = b**2-4*a*c
        out['eqn'] = self.equation()
        out['nature'] = self.nature()
        discriminant_print = 'discriminant = ' + str(self.discriminant)
        out['dsc'] = discriminant_print
        if self.discriminant >= 0:
            out['roots'] = self.proceedure()
        else:
            out['roots'] = ''
        return out