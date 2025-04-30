import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

class calculatot(graphene.ObjectType): # it is the object type of graphene
    concat = graphene.String() # this is field of the object type
    add = graphene.String() # this is field, each filed as a resolver method

    def resolve_concat(self, info): # this is done to tell, how fields will be retrieved
        return "This is a concatenation of two strings"

        #  this is the standard naming convention for resolver methods
    def resolve_add(self, info): 
        return "This is a sum of two numbers"
    

app = FastAPI()

app.mount("/", GraphQLApp(
    schema=graphene.Schema(query=calculatot),
    on_get=make_graphiql_handler(),  # Enables GraphiQL UI in browser
))