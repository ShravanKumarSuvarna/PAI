def fuzzy_union(set1, set2):
    return {element: max(set1.get(element, 0), set2.get(element, 0)) for element in set1.keys() | set2.keys()}

def fuzzy_intersection(set1, set2):
    return {element: min(set1[element], set2[element]) for element in set1.keys() & set2.keys()}

def display_fuzzy_set(fuzzy_set):
    print("{" + ", ".join([f"{element}: {membership}" for element, membership in fuzzy_set.items()]) + "}")

# Example fuzzy sets
set1 = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
set2 = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'f': 0.9, 'g': 0.4}

print("Fuzzy set 1:")
display_fuzzy_set(set1)

print("\nFuzzy set 2:")
display_fuzzy_set(set2)

print("\nUnion of the fuzzy sets:")
display_fuzzy_set(fuzzy_union(set1, set2))

print("\nIntersection of the fuzzy sets:")
display_fuzzy_set(fuzzy_intersection(set1, set2))
