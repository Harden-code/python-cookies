from typing import overload, Union


def tag(name, *content, class_=None, **attrs):
    if class_:
        attrs['class'] = class_

    pairs = (f'{key}={val}' for key, val in attrs.items())
    str_pairs = ''.join(pairs)
    # 如果没参数默认是()
    if content:
        elements = [f'<{name} {str_pairs}>{c}</{name}>' for c in content]
        return '\n'.join(elements)
    else:
        return f'<{name}{str_pairs}>'


print(tag(content='con', name='p'))


class Max:
    @overload
    def max_(self, __Iterate, other) -> Union[int, float]:
        ...

    def max_(self, __Iterate, other) -> Union[int, float]:
        print(other)
        return max(__Iterate)

    @overload
    def max_(self, __Iterate, other, flag=False) -> Union[int, float]:
        ...
    # __表示位置参数

    def max_(self, __Iterate, other, flag=False) -> Union[int, float]:
        if flag:
            print(other)
        return max(__Iterate)


m = Max()

m.max_([1, 23, 4], 'help')
