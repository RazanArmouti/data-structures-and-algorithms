# Challenge Summary
Review the pseudocode for **Quick sort**, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

## Blog
[blog](BLOG.md)

## Whiteboard Process
![quick-sort](quick_sort.png)

## Approach & Efficiency
- Time : O(nLogn).
- space : O(1)
This is a divide-and-conquer algorithm, so, best case, it takes O(n log n) time—that’s n steps to partition the array, log n times.
Since at any step in the process, it only swaps elements within the array, it uses O(1) space.

## Solution
after cloneing the repo navigate to `python/code_challenges/quick_sort ` directory then run `poetry shell` and `poerty install` then run `pytest`
![test](test.png)
