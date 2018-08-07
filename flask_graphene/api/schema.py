import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import Reading, Device
from flask_graphene import app, db


class ReadingNode(SQLAlchemyObjectType):
    class Meta:
        model = Reading
        interfaces = (graphene.relay.Node,)


class ReadingConnection(graphene.relay.Connection):
    class Meta:
        node = ReadingNode


class CreateReading(graphene.Mutation):
    reading = graphene.Field(ReadingNode)
    ok = graphene.Boolean()

    class Arguments:
        deviceid = graphene.Int(required=True)
        temperature = graphene.Float()
        humidity = graphene.Float()
        createdatetime = graphene.String()

    def mutate(self, info, deviceid, **kwargs):
        app.logger.info(kwargs)

        reading = Reading(deviceid=deviceid, **kwargs)
        db.session.add(reading)
        db.session.commit()
        ok = True

        return CreateReading(reading=reading, ok=ok)


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


class Mutation(graphene.ObjectType):
    create_reading = CreateReading.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

