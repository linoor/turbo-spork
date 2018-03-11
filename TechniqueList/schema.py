import graphene
from graphene_django import DjangoObjectType

from TechniqueList.models import Position, Group, Technique


class PositionType(DjangoObjectType):
    class Meta:
        model = Position

class GroupType(DjangoObjectType):
    class Meta:
        model = Group

class TechniqueType(DjangoObjectType):
    class Meta:
        model = Technique

class Query(graphene.ObjectType):
    all_positions = graphene.List(PositionType)
    all_groups = graphene.List(GroupType)
    all_techniques = graphene.List(TechniqueType)

    def resolve_all_positions(self, info, **kwargs):
        return Position.objects.all()

    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.select_related("position").all()

    def resolve_all_techniques(self, info, **kwargs):
        return Technique.objects.select_related("group").all()

schema = graphene.Schema(query=Query)