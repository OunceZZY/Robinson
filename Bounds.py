"""
Define Bounds
"""
import Bound
class Bounds:
    def whatami(self):
        return "Bounds"

    def __init__(self, toCpy=None):
        self.bounds = []
        if toCpy is not None:
            if not isinstance(toCpy, Bounds):
                raise Exception("Not a Bounds Var, a " + str(type(toCpy))+ " given" )
            L = toCpy.getBounds()
            for e in L:
                self.bounds.append(e)

    def __len__(self):
        return len(self.bounds)

    def cpy(self, BoundsType):
        ret = BoundsType()
        for e in self.bounds:
            ret.union(e.cpy())
        return ret

    def __str__(self):
        ret = "{"
        B = self.bounds
        m = len(B)
        for i in range(m):
            ret += str(B[i])
            if i < m-1:
                ret+= ","
        ret += "}"
        return ret

    def getBounds(self):
        return self.bounds


    def union(self, elt:Bound):
        # default union move
        self.bounds.append(elt)

    def causes_contradiction(self, otherB):
        """
        self is a lowerbounds, otherB is a upperbounds
        :param otherB:
        :return:
        """
        if len(self.bounds)==0 or len(otherB)==0:
            return False
        L = self.bounds
        U = otherB.getBounds()
        for u in U:
            for l in L:
                if u == l or u <= l:
                    return True
        return False