import datetime
import pprint

import pymongo
import pymongo as pyM

# Cria uma conexão com o banco de dados local
client = pyM.MongoClient("mongodb://localhost:27017/")

# Cria um objeto do banco de dados
db = client.test

collection = db.test_collection
print(collection)

# Criando documento para inserir no banco
post = {
    'author':'Mike',
    'text':'My first mongoDb application based on Python',
    'tags':['mongodb', 'python', 'pymongo'],
    'date': datetime.datetime.utcnow()
}
#
posts = db.posts
# post_id = posts.insert_one(post).inserted_id
#print(post_id)

'''print(db.posts)
print('\n')
print(db.list_collection_names())
print('\n')
print(db.posts.find_one()) #imprime o arquivo enviado
print('\n')
pprint.pprint(db.posts.find_one()) # imprime por ordem alfabética das chaves
print('\n')
pprint.pp(db.posts.find_one()) #impime o documento com as chaves na ordem original
print('\n')
'''
# bulk intsert '''
'''
new_posts = [
    {
        'author': 'gustavo',
        'text':'learned mongoDb application based on Python',
        'tags':['django', 'flask', 'fastapi'],
        'date': datetime.datetime.now()
    },
    {
        'author': 'luanna',
        'text':' mongoDb application based on Python',
        'tags':['sql', 'nosql', 'db'],
        'date': datetime.datetime.now()
    }
]
'''
'''for item in new_posts:
    pprint.pprint(item)
    print('\n')'''
'''
result = posts.insert_many(new_posts)
print(result.inserted_ids)
pprint.pprint(db.posts.find_one({'author':'gustavo'})) # traz a primeira ocorencia q encontrar
print('\n')
'''
'''for post in posts.find(): # vai no banco e me traz os documentos na coleção posts
    pprint.pprint(post)
    print('\n')
'''
print(posts.count_documents({'author':'Mike'}))
print(posts.count_documents({'author':'gustavo'}))
pprint.pprint(posts.count_documents({'author':'luanna'}))
print('\n')
'''
print('Recuperando documentos e ordenando por data')
for post in posts.find({}).sort('date'):
    pprint.pprint(post)
    print('\n')
'''
# crindo indice para os documentos
indice = db.profiles.create_index([('tags', pymongo.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile =[
    {'user_id':'211', 'name':'Dexter' },
    {'user_id':'212', 'name':'Kiki' }
]
# inserindo documento(user_profile) na coleção profiles_user
'''db.profiles_user.insert_many(user_profile)'''

collections = db.list_collection_names()
print('COLEÇÕES')
for collection in collections:
    print(collection.title())

# Remove um documento
# db.profiles_user.delete_many({'user_id': '211'})

# Verifica se o documento foi removido
resultado = db.profiles_user.find_one({'user_id': '211'})
if resultado is None:
    print('Documento removido com sucesso!')
else:
    print('Erro ao remover documento.')

# Remove uma collection
db.profiles.drop()
collections_two = db.list_collection_names()
print('\nColeções depois do drop')
for collection in collections_two:
    pprint.pprint(collection)

print(posts.count_documents({'author':'Mike'}))
print(posts.count_documents({'author':'gustavo'}))
print(posts.count_documents({'author':'luanna'}))
print('\n')
print('Deletando arquivo por qlquer chave')
db.posts.delete_one({'author':'Mike'})
db.posts.delete_one({'tags':'nosql'})
db.posts.delete_one({'text':'learned mongoDb application based on Python'})

print(posts.count_documents({'author':'Mike'}), 'Mike')
print(posts.count_documents({'author':'gustavo'}), 'Gustavo')
print(posts.count_documents({'author':'luanna'}), 'Luanna')
print('\n')
