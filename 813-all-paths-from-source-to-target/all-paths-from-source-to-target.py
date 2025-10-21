class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph:
            return []
        
        res = []
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(list(path))
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor,path)
                path.pop()
            
        dfs(0,[0])
        return res




        
        
