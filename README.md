# Assignments
Assignment 1 - Create Mathematical Tables from 3 to 20    
1a) Create Mathematical Tables from 3 to 20 through hard-coding   

3 * 1 = 3    
3 * 2 = 6     
3 * 3 = 9     
3 * 4 = 12     
3 * 5 = 15     
3 * 6 = 18     
3 * 7 = 21    
3 * 8 = 24    
3 * 9 = 27    
3 * 10 = 30          

4 * 1 = 4     
4 * 2 = 8     
.........    
4 * 10 = 40    


20 * 1 = 20     
20 * 2 = 40     
...........    
20 * 10 = 200.     

1b) Take input from the keyboard and generate the same result
start = input ("Enter first number")    
end = input ("Enter second number")    

1c) Take input from a file in1.txt containing 3 in first line and 8 in second line and generate the mathematical tables
3    
8     

1d) Take input from a file in2.txt containing 3,8 in the first line and generate the mathematical tables     
3,8    
   
1e) Send the results to an output file out1.txt.  Use "\n" wherever required to generate a new line. The file content should look same as the console output

1f) Send the results to 6 different output files 3.txt, 4.txt, 5.txt, 6.txt, 7.txt, 8.txt depending on the start and end values given as input.  ie. The output filename should be dynamically created for each and every mathematical table generated

1g) Using Python-Django, show the above Mathematical Tables from 3 to 8 as a dynamic HTML page like http://127.0.0.1:5000/tables.  The Python logic should be in a function inside views.py    

1h) Using Python-Django, take the inputs "start" and "end" as HTML Form inputs and generate the dynamic HTML page showing Mathematical Tables    


Assignment 2 - Simple Calculator

2a) Create a simple calculator to take two integer numbers and print the following in one single line
sum1 - n1+n2
dif1 - n1-n2
prd1 - n1*n2
div1 - n1/n2
div2 - n1//n2
rem1 - n1%n2
exp1 - n1**n2
print(sum1, dif1, prd1, div1, div2, rem1, exp1)

2b) Create a function calc1(n1, n2) to take the 2 input values and print the output

2c) Create a function calc2(n1, n2) to take the 2 input values, create a list list1, append all results to this list and return this list to the main program
list1.append(sum1)
list1.append(dif1)
list1.append(prd1)
list1.append(div1)
list1.append(div2)
list1.append(rem1)
list1.append(exp1)
return list1

In the main program, create a variable to catch the returned value and process it to print the required values
result = calc1(8,4)
print(result)

## Assignment 3 - School Clock Angle
School Clock is showing 9 am.  Compute the angle between the Hour hand and the Minute hand.  It should show Time: Angle in Degrees from 9:00 am to 8:55 pm with a spacing of 5 minutes.  
![Clock at 9:00 am](https://github.com/ckuthyar/python3/blob/main/Clock_900.png)
Clues
1) What is the exact angle between Hour Hand and Minute Hand at 9 am ?
2) What is the exact angle between Hour Hand and Minute Hand at 9:05 pm ?
3) What is the exact angle between Hour Hand and Minute Hand at 9:10 pm ?
4) What is the exact angle between Hour Hand and Minute Hand at 9:15 pm ? 
5) What is the speed of the hour hand ? ie    
In one hour, how many degrees doe it move ?      
In one minute, how many degrees does it move ?     
In 5 minutes, how many degrees does it move ?    

Output should be

09:00 - 90 degrees    
09:05 -  ...   degrees    
09:10 -  ....  degrees    
.........    
9:55 -     


10:00 -    
10:05 -    
.........    
10:55 -    


11:00 -    
11:05 -    
........    
11:55 -    



20:00 -    
20:05 -    
.....    
20:55 -   


## Assignment 4 - Andaman Prisoner Problem    
4a) There are 100 prison cells in a row. All cells are locked. Jailer is given permission by the Prime Minister of India to release any number of prisoners.     
In Round 1, Jailer opens all the doors.   
In Round 2, he closes every alternate door (2, 4, 6...).   
In Round 3, every third door (3, 6, 9,....) if Door is Open,, he closes it. If Door is Closed, he opens it.   
In Round 4, every fourth door (4, 8, 12..), if Door is open,, he closes it. If Door is Closed, he opens it.    
He does this for 100 Rounds. At the end, who are the lucky prisoners ?    

![Andaman Prisoner](https://github.com/ckuthyar/python3/blob/main/Tech_FwP_AndamanPrisoner_1.png)    
4b) Prepare 2 letters. Letter1 to PM giving list of lucky prisoners and release date as today. Letter2 to Jailer giving list of unlucky prisoners who will be released after 4 weeks.    

## Assignment 5 - Gold Medal Problem    
