Here simplar to problem 5 we are using trie data structure
We store handler to each part and instead of storing a single character we store complete word(part)

RouteTrie will store all routes with their handlers.

To find an route handler we iteratively go deep inside router to find the respective handler.

We use backtracking to find the respective handlers

Here we split path into parts and ignore empty strings. 

    e.g. /home/about/me => [home,about,me]

It works with and without a trailing slash


Time Complexity - O(N) As it will parse complete path to get handler
Space Complexity - O(1) As we only use few temporary variables
