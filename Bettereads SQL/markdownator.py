def createTable(things):
    maxim = max(map(len, things))

    table = '|' + '-' * maxim + '|'

    return table

def fileTable(name, things):
    file = open(name + ".md", "w")
    file.write(createTable(things))
    file.close()
        

things = ["rock", "paper", "scissors"]
fileTable("rps_test", things)