# Hashmap LEFT JOIN
returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

**Syntax :**
```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```
![leftJoin](https://www.w3schools.com/sql/img_leftjoin.gif)

## Challenge
Implement a simplified LEFT JOIN for 2 Hashmaps.

- Write a function called left join
- Arguments: two hash maps
    + The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    + The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard
![hashmap-left-join](assets/hashmap-left-join.png)
## Approach & Efficiency
- Time : O(n)
- space : O(n)

## Solution
after cloneing the repo navigate to `python/hashmap_left_join ` directory then run `poetry shell` and `poerty install` then run `pytest`
