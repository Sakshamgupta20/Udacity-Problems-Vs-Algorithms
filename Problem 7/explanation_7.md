Here we split path into parts and ignore empty strings. 

    e.g. /home/about/me => [home,about,me]

It works with and without a trailing slash


Time Complexity - O(N) As it will parse complete path to get handler
Space Complexity - O(1) As we only use few temporary variables
