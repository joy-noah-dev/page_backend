from graphene import ObjectType, String, Schema

class ExampleQuery(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "world"


class RootQuery(ExampleQuery, ObjectType):
    pass


schema = Schema(query=RootQuery)