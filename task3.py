def list_declaration():
    # Zadeklaruj listę skłądającą się z 4 elementów określonych typów,
    # kolejno: `string`, `int`, `float` i `bool`
    result: list = ["abcd", 123, 5.44, False]
    return result


def list_indexing(a: list):
    # Do zmiennych zadeklarowanych poniżej przypisz pierwszy (zmienna `first`)
    # i ostatni (zmienna `last`) element listy przekazanej jako argument `a`
    first: int = a[0]
    last: int = a[-1]

    return first, last


def list_sum(a: list):
    # Przypisz do zmiennej `result` sumę wszystkich elementów listy `a`
    result: int = sum(a)
    return result


def dict_declaration():
    # Zadeklaruj słownik, który pod kluczem `line_length` będzie miał wartość 42
    my_dict: dict = {'line_length': 42}

    return my_dict


def dict_retrieving_values(mapping: dict):
    # Zsumuj ze sobą wartości spod kluczy `a` i `b` ze słownika `mapping`
    sum: int = mapping['a'] + mapping['b']
    return sum


def dict_pass_values(dict_a, dict_b):
    # Przepisz wartość spod klucza "variable" ze słownika `dict_a` do `dict_b`

    dict_b['variable'] = dict_a['variable']

    return dict_b


def set_declaration():
    # Zadeklaruj zbiór składający się z samych liczb typu `int`
    my_set: set= set([1, 2, 3, 4, 5])

    return my_set


def set_operations(set_a: set, set_b: set):
    # Korzystając ze zbiotów `set_a` i `set_b` stwórz zbiory będące kolejno przecięciem, sumą i różnicą
    # tych dwóch zbiorów. Wyniki powyższych operacji przypisz do odpowiadających im zmiennych zadeklarowanych
    # poniżej
    itersection: set = set_a.intersection(set_b)
    union: set = set_a.union(set_b)
    difference: set = set_a.difference(set_b)

    return itersection, union, difference


def set_add_list(values_set: set, values_list: list):
    # Uzupełnij zbiór `values_set` o wartości z listy `values_list`
    result: set = values_set.union(values_list)
    return result
