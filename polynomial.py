class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate (self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate (self, x):         #Eval
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate (self, x):         #Eval
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate (self, x):         #Eval
        return self.p1.evaluate(x) * self.p2.evaluate(x)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)


#excercise B
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate (self, x):           #Eval
        return self.p1.evaluate(x) - self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p2 == 0:
            raise ValueError("Division by zero")
        
    def __repr__(self):
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
    
    def evaluate (self, x):             #Eval
        denominator = self.p2.evaluate(x)
        if denominator == 0:
            raise ValueError("Division by zero")
        return self.p1.evaluate(x) / denominator

poly = Add( Sub( Int(4), Int(3)), Sub( X(), Div( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)


    