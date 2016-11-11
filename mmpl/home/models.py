from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


# Abstract Link Class
class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class HomePage(Page):
    pass


# Social Snippet
@register_snippet
class Social(LinkFields):
    title = models.CharField(max_length=50, verbose_name="Social Site")
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='social',
        null=True,
        blank=True
    )
    icon = models.CharField(max_length=20, verbose_name="Icon Code (fa)")

    panels = [
        FieldPanel('title', classname='full title'),
        FieldPanel('link_external'),
        FieldPanel('icon')
    ]

    def __unicode__(self):
        return self.title


# Copyight Snippet
@register_snippet
class Copyright(models.Model):
    copyright = models.CharField(
        max_length=100,
        verbose_name="Copyright Footer"
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='copyright',
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('copyright', classname='full title')
    ]

    def __unicode__(self):
        return self.copyright


# Footer Snippet
@register_snippet
class AboutFooter(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Header"
    )
    body = models.CharField(
        max_length=500,
        verbose_name="Body"
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='footer_about',
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('title', classname='full title'),
        FieldPanel('body')
    ]

    def __unicode__(self):
        return self.title


# Logo Snippet
@register_snippet
class Logo(models.Model):
    description = models.CharField(
        max_length=100,
        verbose_name="Description"
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='logo',
        null=True,
        blank=True
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='image'
    )

    panels = [
        FieldPanel('description', classname='full title'),
        ImageChooserPanel('image')
    ]

    def __unicode__(self):
        return self.description
