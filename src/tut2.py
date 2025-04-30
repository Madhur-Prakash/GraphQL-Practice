import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# class course(graphene.ObjectType):
#     name = graphene.String()
#     duration = graphene.Int() 

#     def resolve_name(self, info): 
#         return "This is a course name" 

      
#     def resolve_duration(self, info): 
#         return "This is a course duration"
    

data = [
    {
        "name": "Python",
        "city": "New York",
    },
    {
        "name": "Java",
        "city": "Los Angeles",
    },
    {
        "name": "JavaScript",
        "city": "Chicago",
    }
]


class language(graphene.ObjectType):
    name = graphene.String()
    city = graphene.String()

    
class person(graphene.ObjectType):
    lang = graphene.List(language)
    def resolve_lang(self, info):
        return data


app = FastAPI()
app.mount("/",GraphQLApp(
    schema=graphene.Schema(query=person),
    on_get=make_graphiql_handler(),  # Enables GraphiQL UI in browser
))
print(graphene.Schema(query=person))
