>>> import pprint
>>> lst = list(range(5))
>>> pprint.pprint(lst)
[0, 1, 2, 3, 4]
>>> mtx = [list(range(5)) for _ in range(5)]
>>> pprint.pprint(mtx)
[[0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4]]
>>> mtx2 = [list(range(x)) for x in range(5)]
>>> pprint.pprint(mtx2)
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
>>> abc = [chr(65 + x) for x in range(5)]
>>> abc
['A', 'B', 'C', 'D', 'E']
>>> mtx_abc = [[chr(65 + (x * 5) + i) for i in range(5)] for x in range(5)]
>>> pprint.pprint(mtx_abc)
[['A', 'B', 'C', 'D', 'E'],
 ['F', 'G', 'H', 'I', 'J'],
 ['K', 'L', 'M', 'N', 'O'],
 ['P', 'Q', 'R', 'S', 'T'],
 ['U', 'V', 'W', 'X', 'Y']]











