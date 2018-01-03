ch01 README.rd

These are the chapter one exercises as scraped from the PDF. 

1-1. Consider the following statement: “As machines get faster and memory cheaper, algorithms become less
important.” What do you think; is this true or false? Why?

False. 

Because regardless of how much faster the hardware gets it is not going to help you figure out how to solve a problem. Well, AI aside. Once AI can coded better than us we are all out of jobs. 

Algorithms are roadmaps for how to approach and solve a give particular problem and as such I do not believe they are any less important now then they ever were. Knuth would be dissapointed in you for ever even suggesting otherwise. :/

1-2. Find a way of checking whether two strings are anagrams of each other (such as "debit card" and "bad credit").
How well do you think your solution scales? Can you think of a naïve solution that will scale poorly?

Off the top of my head I would say take advantage of Python's ordered lists, iterate over each string and put it in a list, then sort the resulting lists and check if they are ==. 

