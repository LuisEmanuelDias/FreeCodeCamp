def arithmetic_arranger(problems,condition=False):
    
    solution = []
    solutions = []
    m=0
    firstline = ""
    secondline = ""
    thirdline = ""
    forthline = ""
    simbol = ""
    for count in problems:
      # Here I split the problems and solves them
        if count.find("+")+1:
            simbol = "+"
            solution = count.rsplit("+")
            try:
              solutions += [int(solution[0])+ int(solution[1])]
            except:
              return "Error: Numbers must only contain digits."
        elif count.find("-")+1:
            simbol = "-"
            solution = count.rsplit("-")
            try:
              solutions += [int(solution[0])- int(solution[1])]
            except:
              return "Error: Numbers must only contain digits."
        else:
          return "Error: Operator must be '+' or '-'."
        if len(solution[0].strip())>4 or len(solution[1].strip())>4:
          return "Error: Numbers cannot be more than four digits."
        #Here I create the 4 lines to return them
        space = max(len(solution[1].strip()),len(solution[0].strip()))+2
        firstline += " "*(space-len(solution[0].strip())) +solution[0].strip()+" "*4
        secondline += simbol+ " "*(space-len(solution[1].strip())-1)+solution[1].strip()+" "*4
        thirdline += "-"*space + " "*4
        forthline += " "*(space-len(str(solutions[m])))+ str(solutions[m])+" "*4
        m+= 1
    if m>5: 
      return "Error: Too many problems."   
    arranged_problems = firstline.rstrip()+"\n"+secondline.rstrip()+"\n"+thirdline.rstrip()
    if condition:
        arranged_problems +="\n"+forthline.rstrip()
    return arranged_problems