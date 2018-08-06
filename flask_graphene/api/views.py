from flask_graphql import GraphQLView

from . import blueprint_api
from .schema import schema


blueprint_api.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

