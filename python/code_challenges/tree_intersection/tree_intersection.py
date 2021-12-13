from hash_table import HashTable
def tree_intersection(first_tree , second_tree):
    tree1 = first_tree.pre_order()
    tree2 = second_tree.pre_order()

    if not tree1 and not tree2:
        raise Exception("Empty trees !!!")
    if not tree1 or not tree2:
        raise Exception("There is no another tree to find the intersection")
    values_founded =[]
    hash_table = HashTable()
    for node in tree1:
        hash_table.add(str(node),node)
    for node in tree2:
        if hash_table.contains(str(node)):
            values_founded.append(node)
        else :
            hash_table.add(str(node),node)

    if not values_founded:
        return "there is no intersection between these trees"
    return values_founded
