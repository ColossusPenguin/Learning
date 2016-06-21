from __future__ import division

def evaluate(exp):
    "Evaluate Exp, or return 'NONE' if there is an arithmetic error"
    try: 
        return eval(exp)
    except ArithmeticError:
        return None
        
def solve_no_brackets(years, ops=('+', '-','*', '/')):
    "All Solutions to the Countdown Puzzle without Brackets"
    exps=('10'+a+'9'+b+'8'+c+'7'+d+'6'+e+'5'+f+'4'+g+'3'+h+'2'+i+'1'
        for a in ops
        for b in ops
        for c in ops
        for d in ops
        for e in ops
        for f in ops
        for g in ops
        for h in ops
        for i in ops)

    return {int(evaluate(exp)): exp
        for exp in exps if evaluate(exp) in years}

        
%time solve_no_brackets(years=range(1900, 2100))


c10 = (10,9,8,7,6,5,4,3,2,1)

def splits(items):
    "Split sequence into two non-empty parts, in all ways"
    return [(items[:i], items[i:])
    for i in range(1,len(items))]
    
splits(c10)

exps[(10,9,8)]
