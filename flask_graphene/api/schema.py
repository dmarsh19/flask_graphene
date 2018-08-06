import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Reading, Device


class ReadingNode(SQLAlchemyObjectType):
    class Meta:
        model = Reading
        interfaces = (graphene.relay.Node,)


class ReadingConnection(graphene.relay.Connection):
    class Meta:
        node = ReadingNode


class DeviceNode(SQLAlchemyObjectType):
    class Meta:
        model = Device
        interfaces = (graphene.relay.Node,)


class DeviceConnection(graphene.relay.Connection):
    class Meta:
        node = DeviceNode


class Query(graphene.ObjectType):
    reading = graphene.relay.Node.Field(ReadingNode)
    all_readings = SQLAlchemyConnectionField(ReadingConnection)

    device = graphene.relay.Node.Field(DeviceNode)
    all_devices = SQLAlchemyConnectionField(DeviceConnection)


schema = graphene.Schema(query=Query)

