from typing import Any, Sequence

import factory
from django.utils.text import slugify
from factory import Faker, LazyAttribute, post_generation
from factory.django import DjangoModelFactory
from guardian.shortcuts import assign_perm

from demanage.organizations.models import Organization
from demanage.users.tests.factories import UserFactory


class OrganizationFactory(DjangoModelFactory):
    name = LazyAttribute(
        lambda _: Faker("company").evaluate(None, None, {"locale": None})[:50]
    )
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    public = factory.Iterator([True, False])
    website = Faker("url")
    location = Faker("country_code")
    verified = factory.Iterator([True, False])
    representative = factory.SubFactory(UserFactory)

    @post_generation
    def assign_permissions(obj, create: bool, extracted: Sequence[Any], **kwargs):
        if not create:
            return

        for perm in [
            # Organization
            "organizations.view_organization",
            "organizations.change_organization",
            "organizations.delete_organization",
            # Member
            "organizations.view_member",
            "organizations.invite_member",
            "organizations.kick_member",
        ]:
            assign_perm(perm, obj.representative, obj)

    class Meta:
        model = Organization
        django_get_or_create = ["slug"]
