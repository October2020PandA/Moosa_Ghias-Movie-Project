faraz = []
abdullah = [] 
noman = [] 

movies = ['up','transformers','mission impossible']

for m in movies: 
    print('Do you want to watch movie '+movies[m])
    response_faraz =  input('Farz response').lower()
    response_abdullah =  input('abdullah response').lower()
    response_noman =  input('Noman response').lower()
    faraz.append(response_faraz)
    abdullah.append(response_abdullah)
    noman.append(response_noman)
    print("loop ran")

#for f in faraz: 
 #   if (faraz[f] and abdullah[f] and noman[f]) == 'y'):
 #       print(movies[f])