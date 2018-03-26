from pydash import _
from string import Template

findNonZero = _().find_last_index(lambda elem: elem != 0)
checkForZero = lambda x: x if x > 0 else 0
checkCoeffList = _.flow(findNonZero, checkForZero)
sliceZeroCoeffs = lambda coeffs_list: _.slice(coeffs_list, 0, checkCoeffList(coeffs_list) + 1)

size = lambda list: _.size(list)

append = lambda appends, list: list + appends
curryLeftAppend = _.curry(append)
curryRightAppend = _.curry_right(append)

isNumerical = lambda x: isinstance(x, (int, float))
isListEmpty = lambda list: size(list) == 0
isListNumerical = _().every(isNumerical)

addToFirstElem = _.curry(lambda value, list: [list[0] + value] + list[1:])
sumIdenticalSizeList = lambda a_list, b_list: _.map(a_list, lambda x, index: b_list[index] + x)
# size b gt size a
sumGtList = lambda a, b: _.flow(sumIdenticalSizeList, curryLeftAppend(_.slice(b, size(a), size(b))))(a, b)
sumList = lambda a, b: sumGtList(a, b) if size(b) > size(a) else sumGtList(b, a)

polyTemplate = Template('${type} ${coeff}x${degree} ')
stringifyPolynomial = _().reduce(lambda total, x, index: total + polyTemplate.substitute(type='+' if x >= 0 else '-', coeff=abs(x), degree=index), '')

valueList = _.curry(lambda item, length: map(item, range(length)))
zeroList = valueList(lambda _: 0)
listMulOnValue = lambda num: _().map(lambda x: num * x)
polyMulMonome = lambda degree, num, list: _.flow(listMulOnValue(num), curryRightAppend(zeroList(degree)))(list)

def list_insert(lst, item):
  lst.append(item)
  return lst

polynomialMul = lambda a,b: _.reduce(a, lambda total, coeff, index: list_insert(total, polyMulMonome(index, coeff, b)), [])
flatSumList = lambda x: _.reduce(x, lambda total, poly: sumList(total, poly), [])

polyMul = lambda a,b: _.flow(polynomialMul, flatSumList)(a,b)
