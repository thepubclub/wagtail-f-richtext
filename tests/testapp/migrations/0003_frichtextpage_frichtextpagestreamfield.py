# Generated by Django 3.2.15 on 2022-09-10 20:48

import django.db.models.deletion
from django.db import migrations, models
from wagtail import blocks as wagtail_blocks
from wagtail import fields as wagtail_fields


class Migration(migrations.Migration):
    dependencies = [
        ("tests_testapp", "0002_create_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="FRichTextPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("body", wagtail_fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="FRichTextPageStreamField",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail_fields.StreamField(
                        [
                            (
                                "rich_text",
                                wagtail_blocks.RichTextBlock(
                                    template="blocks/f_richtext_block.html"
                                ),
                            )
                        ],
                        use_json_field=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
