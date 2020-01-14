class fibo_c:
      def __init__(self, number):
            self.number = number                                                
      def fibonacci_series(self):
            with open('C:/Users/OLUWADAMILARE/Desktop/Fibonacci Result.txt', 'a') as save_s:
                  save_s.write('\n \n===>    The Fibonacci series of  '
                               + str(user_input)+ '  is listed below     <===\n')
            a, b= 0, 1
            list1 = []
            while True:
                  a, b = b, a+b
                  list1.append(a)
                  if a > self.number:
                        break
                  print(a)
            with open('C:/Users/OLUWADAMILARE/Desktop/Fibonacci Result.txt', 'a') as save_s:
                  save_s.write(str(list1)+'\n       The length of your'+
                               ' Fibonacci series is '+str(len(list1))+'!')
            print('       The length of your Fibonacci series is ',len(list1))                 
print('Welcome User! ')
while  True:
      try:
            user_input = int(input('Enter the Fibonacci series' +
                                   'you need to save or \'0\' to Quit: '))
            if user_input == 0:
                  print('\nThank You, stay updated for more console'+
                        ' based apps!\nDev.Damilare')
                  break
            else:
                  ans_fibo = fibo_c(user_input) 
                  print('  ==>  The Fibonacci series of  the value ', user_input, ''+
                        'you entered is listed below....')
                  ans_fibo.fibonacci_series()
      except TypeError:
            print('Please enter a valid number! ')
      except ValueError:
             print('Please enter a valid number! ')
