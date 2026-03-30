while True:
    try:
        
        R, C, M = map(int, input().split())
        
        
        matrix = []
        for _ in range(R):
            row = list(map(int, input().split()))
            matrix.append(row)
        
       
        if M > 0:
            operations = list(map(int, input().split()))
        else:
            operations = [] 
            
        operations = operations[::-1]

        
        for op in operations:
            if op == 0:
                matrix = [list(row) for row in zip(*matrix)][::-1]
            elif op == 1:
                matrix = matrix[::-1]
                
        
        print(len(matrix), len(matrix[0]))
        
        
        for row in matrix:
            print(*row)

    
    except (EOFError, ValueError):
        break
