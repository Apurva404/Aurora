Implementation
--------------
The implemented scheduler is employing a simple greedy approach.

It reads in a list of buildings and constructs a resource requirement map out of it.
Using the list of employees and their availibility during the week, it constructs another map that depicts avaialble capacity of workers during the entire week.

The algorithm greedily services buildings on the first day when their requirements are met. To do so, it goes through each day and try to see if that day's available worker capacity can handle the job or not. If yes, then it reserves the resources, otherwise it tries to service the building the next available day.

It should be noticed that the various class of employees have a hierarchy built into them as per the building requirement criteria, viz.

certified installers > pending certification installers > laborers

As a result, we employed an optimization that whenever we have a choice between laborer, pending certification installer or certified installer, we always choose the lowest priorirty person that fits the bill.

Some of the criteria in the specification mentions that multiple roles could fill a requirement. To model these floating requirements, we used inheritence. And a result, we have classified all employees as certified/non-certified. Further more non-certified employees can be pending certification installer / laborer. This inheritence + the hardcoded logic to choose the employee type with least priority to fill a floating role can be seen in action in scheduler.py line 129, 149.


Tests
-----
We have added few tests that showcases the correctness of the solution in the most common scenarios, as well as some edge cases where this simple algorithm won't be able to find an optimal solution. Additionally, the last test case showcases, how we can tweak the input to priortize certain kind of resource heavy buildings to still get a workable schedule.

How to run
----------
```
>python3 test.py 
```
will run all the tests and print out the schedule in a human readable format.
However the core scheduling engine is separate from the test file, and can be easily integrated in other piece of code that wants to handle the output in a different way (say write to file or print on paper).
