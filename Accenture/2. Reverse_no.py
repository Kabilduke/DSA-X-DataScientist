Question:
Arun is a bus conductor. His ticket machine is pricing in reverse order due to a technical glitch. As a programmer on the bus, you are asked
to help him by creating a program to display the number correctly

////
Solution:
a = int(input())

reverse = int(str(a)[::-1])

print("Ticket: ", reverse)
////

Input:
320

Output:
23
