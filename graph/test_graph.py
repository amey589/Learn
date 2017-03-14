from example import G,G_dir
from graph import Graph
import unittest

class testGraphMethods(unittest.TestCase):
    def test_init(self):
        g1 = Graph(G)
        self.assertEqual(len(g1.visited),len(G),"visited length correct")
        self.assertEqual(g1.visited['a'],False,"visited set to false correctly")
    
    def test_dfs_init(self):
        g1 = Graph(G)
        self.assertEqual(len(g1.visited),len(G),"visited length correct")
        self.assertEqual(g1.visited['a'],False,"visited set to false correctly")
        g1.dfs()
        self.assertEqual(len(g1.traversal),len(G),"traversal list len is correct")

if __name__ == '__main__':
    unittest.main()
