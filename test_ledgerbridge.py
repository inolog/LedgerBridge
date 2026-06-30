# test_ledgerbridge.py
"""
Tests for LedgerBridge module.
"""

import unittest
from ledgerbridge import LedgerBridge

class TestLedgerBridge(unittest.TestCase):
    """Test cases for LedgerBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerBridge()
        self.assertIsInstance(instance, LedgerBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
