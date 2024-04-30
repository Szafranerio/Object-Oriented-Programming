from bank_account import *

Dave = BankAccount(1000, 'Dave')
Sara = BankAccount(2000, 'Sara')
Tom = BankAccount(5400, 'Tom')
Bartek = BankAccount(10000, 'Bartek')
Matthew = BankAccount(2313, 'Matthew')

Dave.getBalance()
Sara.getBalance()
Tom.getBalance()
Bartek.getBalance()
Matthew.getBalance()

Sara.deposit(500)
Dave.deposit(45)
Bartek.deposit(654)

Dave.withdraw(10000)
Sara.withdraw(10)

Dave.transfer(10000, Sara)
Bartek.transfer(456, Sara)

Jim = InterestRewardsAccount(1000, 'Jim')
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)
Jim.getBalance()

Blake = SavingsAccount(10000, 'Blake')
Blake.getBalance()
Blake.deposit(1000)
Blake.transfer(1234, Sara)
Blake.getBalance()

Sara.getBalance()
