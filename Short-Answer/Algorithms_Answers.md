#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) I believe this is O(n). The condition is active depending on the size of n

b)O(n\*.5n) still chewing on this one

c) O(n) time since we're decrementing by one it will be entirely dependent on n until 0

## Exercise II

I think there are two ways to approach this. One with a linear search O(n), starting with floor 0 and looping through the amount of stories until the first floor to break an egg occurs.

A better way, would be to utilize binary search O(log n). Assuming the floors of the building are ordered/sorted, we start with the middle floor and check if the egg breaks. If it does break, we take the difference between the floors // 2 and first floor, check if break, and continue with the dif until we find the lowest floor of non-breaking egg drop.
