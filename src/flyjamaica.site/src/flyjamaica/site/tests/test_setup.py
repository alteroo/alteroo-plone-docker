# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from flyjamaica.site.testing import FLYJAMAICA_SITE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that flyjamaica.site is properly installed."""

    layer = FLYJAMAICA_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if flyjamaica.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'flyjamaica.site'))

    def test_browserlayer(self):
        """Test that IFlyjamaicaSiteLayer is registered."""
        from flyjamaica.site.interfaces import (
            IFlyjamaicaSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IFlyjamaicaSiteLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = FLYJAMAICA_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['flyjamaica.site'])

    def test_product_uninstalled(self):
        """Test if flyjamaica.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'flyjamaica.site'))

    def test_browserlayer_removed(self):
        """Test that IFlyjamaicaSiteLayer is removed."""
        from flyjamaica.site.interfaces import \
            IFlyjamaicaSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IFlyjamaicaSiteLayer,
           utils.registered_layers())
