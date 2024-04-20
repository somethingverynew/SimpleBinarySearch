def naive_search(l, target):
    for i in range(len(l)):
        if l[i]== target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    
    if low is None:
        low = 0
    if high is None:
        high=len(l) - 1
    
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    
    l = ['kevin', 'john', 'mike', 'fred', 'piglet']
    l.sort()
        
    running = True

    while running:
        target = input("Enter the name your searching for!")
            
        naive_result = naive_search(l, target)
        binary_result = binary_search(l, target)

        if naive_result != -1:
            print(f"Naive Search shows {target} {naive_result + 1} is on page!")
                #adding +1 to index for 'page' number
        else: 
            print(f"{target} is not found using Naive Search")
                
        if binary_result != -1:
            print(f"Binary Search shows {target} {binary_result + 1} is on page!")
                #adding +1 to index for 'page' number
        else:
            print(f"{target} is not found using Binary Search")
                
        search_again = input('Would you like to search again? (yes/no):')

        while search_again.lower() not in ['yes', 'no']:
            print("Invalid entry.")
            search_again = input("Would you like to play again? (yes/no): ")
        if search_again != 'yes':
            
            running = False

print('Goodbye!')