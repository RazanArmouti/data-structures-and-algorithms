from hash_table import HashTable

def left_join(first_hashmap:HashTable, second_hashmap:HashTable):
    final_hashmap = []
    for item in first_hashmap:
        left_join =[]
        left_join.append(item[0])
        left_join.append(item[1])
        if second_hashmap.contains(item[0]):
            left_join.append(second_hashmap.get(item[0]))
        else:
            left_join.append(None)
        final_hashmap.append(left_join)
        if item:
            item.pop(0)
            if item:
                item.pop(0)
    return final_hashmap


if __name__=="__main__":
    first_hash_table = HashTable()
    first_hash_table.add("person", "23")
    first_hash_table.add("person1", "30")
    first_hash_table.add("person2", "27")
    first_hash_table.add("person3", "18")
    first_hash_table.add("person4", "19")
    second_hash_table = HashTable()
    second_hash_table.add("person", "45")
    second_hash_table.add("person1", "25")
    second_hash_table.add("person2", "19")
    second_hash_table.add("person4", "9")

    print(left_join(first_hash_table, second_hash_table))
