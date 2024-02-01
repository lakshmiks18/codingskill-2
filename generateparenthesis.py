class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out=[]
        stack=[]
        def backtrack(openCount=0,closedCount=0):
            #if iteration is complete...
            if(closedCount==n):
                out.append("".join(stack))
            else:
                #open possible?
                if(openCount<n):
                    stack.append('(')
                    backtrack(openCount+1,closedCount)
                    stack.pop()
                #closed possible?
                if(closedCount<openCount):
                    stack.append(')')
                    backtrack(openCount,closedCount+1)
                    stack.pop()
        backtrack()
        return out
