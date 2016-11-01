from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
keyword=[]
r=[]
'''
extarct classes
'''
f=open('123.txt')
for i in f:
	
	tem=i.strip().lower().split()
	
	r.append(" ".join(tem))
	
f.close

#extarct articles
f=open('456.txt')
for i in f:
	
	tem=i.strip().lower().split()
	
	r.append(" ".join(tem))
	keyword.append(" ".join(tem))
f.close

 

counter = TfidfVectorizer(stop_words=stopwords.words('english')).fit_transform(r)

nbrs = NearestNeighbors(n_neighbors=50, algorithm='auto').fit(counter)

distances, indices = nbrs.kneighbors(counter)

res=[]
n=1
for a,b in zip(indices[88:],distances[88:]):
	res.append([n,[],[]])
	for i,j in zip(a,b):
		if i<88 and j<1.34:
			res[n-1][1].append(i+1)
			res[n-1][2].append(j)
		if len(res[n-1][1])>9:break
	n+=1
duos=0
for i in range(len(r)-88):
	#print res[i][0]
	print res[i][1]
	if res[i][1]!=[]:duos+=1
	#print res[i][2]
print float(69-duos)/69




''' 
plural
from nltk.stem import WordNetLemmatizer
WordNetLemmatizer().lemmatize('apples')
'''

