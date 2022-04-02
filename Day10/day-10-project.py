def add(n1, n2):
	return n1+n2

def subtract(n1, n2):
	return n1-n2

def multiply(n1, n2):
	return n1*n2	

def divide(n1, n2):
	return n1/n2


operations = {
	"+":add,
	"-":subtract,
	"*":multiply,
	"/":divide
}


def calculator():

  num1 = float(input("Enter the first number:"))
  for operation in operations:
    print(operation)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Enter a operation from the above list:")
    num2 = float(input("Enter the second number:"))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    next_step = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'exit' to exit: ")

    if next_step == 'y':
      num1 = answer
    elif next_step == 'n':
      should_continue = False
      calculator()
    elif next_step == 'exit':
    	break

calculator()
