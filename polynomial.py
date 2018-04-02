import common as fp

class Polynomial:
    def __init__(self, coefficients):
        if not isinstance(coefficients, list):
            raise TypeError("Coeffs should be list")
        if fp.isListEmpty(coefficients):
            raise TypeError("Empty coeffs")
        if not fp.isListNumerical(coefficients):
            raise TypeError("Coeffs shouild be float or int")
        self.coeffs = fp.prepareCoeefs(coefficients)
        self.degree = fp.size(self.coeffs) - 1

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        if fp.isNumerical(other):
            return Polynomial(fp.addToFirstElem(other)(self.coeffs))
        if isinstance(other, Polynomial):
            return Polynomial(fp.reverse(fp.sumList(self.coeffs, other.coeffs)))
        else:
            raise TypeError()

    def __eq__(self, other):
        if fp.isNumerical(other) and self.degree == 0:
            return other == fp.head(self.coeffs)
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            raise TypeError()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        if fp.isNumerical(other):
            return Polynomial(fp.reverse(fp.listMulOnValue(other)(self.coeffs)))
        if isinstance(other, Polynomial):
            return Polynomial(fp.reverse(fp.polyMul(self.coeffs, other.coeffs)))
        else:
            raise TypeError()

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return fp.stringifyPolynomialPretty(self.coeffs)
