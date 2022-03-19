# Time O(N ^ 2) | Space O(N) - Naive Solution

class Transaction:
    def __init__(self, transaction):
        self.name = transaction[0]
        self.time = int(transaction[1]) 
        self.amount = int(transaction[2])
        self.city = transaction[3]
    
    def toString(self):
        return f"{self.name},{self.time},{self.amount},{self.city}"

def invalidTransactions(transactions):
    transactions = [ Transaction(transaction.split(',')) for transaction in transactions ] # making the input more understandable and readable
    result = []

    for i in range(len(transactions)): # transactions[i] is going to be checked against all other transaction to see if it is valid
        for j in range(len(transactions)):
            if i == j: continue

            amountExceedThousand = transactions[i].amount > 1000
            samePerson = transactions[i].name == transactions[j].name
            transactionWithinSixtyMinute = abs(transactions[i].time - transactions[j].time) <= 60
            differentCity = transactions[i].city != transactions[j].city

            if amountExceedThousand or (samePerson and differentCity and transactionWithinSixtyMinute):
                result.append(transactions[i].toString())
                break # since transaction[i] is invalid. There is no point in staying inside the innerloop. If we stay transactions[i] can be double counted

    return result

# Improved Solution - Sort by time and Do sliding windows between range of 60 minutes for each name

# O(N^2) Worst Time (if every element is inside 60 minute window) | O(NlogN) Average Time
# O(N) Space
def invalidTransactions(transactions):
    transactions = [ Transaction(transaction.split(',')) for transaction in transactions ]
    transactions.sort(key=lambda transaction: transaction.time)
    
    transactionByName = getTransactionsByName(transactions)  # key: name, value: indices[]
    result = []

    for name in transactionByName:
        indices =transactionByName[name]  # Have index of transaction with same name
        left, right = 0, 0
        for idx in indices:
            transaction = transactions[idx]
            if transaction.amount > 1000:
                result.append(transaction.toString())
                continue
            
            while left < len(indices) and transactions[indices[left]].time < transaction.time - 60:
                left += 1
            
            while right < len(indices) and transactions[indices[right]].time <= transaction.time + 60:
                right += 1
                
            for i in range(left, right):
                if transaction.city != transactions[indices[i]].city:
                    result.append(transaction.toString())
                    break
    return result

def getTransactionsByName(transactions):
    transactionByName = {}
    for idx, transaction in enumerate(transactions):
        if transaction.name not in transactionByName:
            transactionByName[transaction.name] = []        
        transactionByName[transaction.name].append(idx)

    return transactionByName
