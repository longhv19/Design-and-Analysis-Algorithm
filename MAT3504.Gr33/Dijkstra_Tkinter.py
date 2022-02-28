#Group 33
# Hướng dẫn sử dụng:
#     - Đúp chuột trái để chọn bắt đầu
#     - Nhấp chuột trái để vẽ chướng ngại vật
#     - Nhấp 1 lần để xóa chướng ngại
#     - Đúp chuột phải để đánh dấu kết thúc

from tkinter import *
import time


class nodeColor():
    START_COLOR = "pink"
    END_COLOR = "green"
    BLOCKED_COLOR = "black"
    FILLED_COLOR_BG = "green"
    CONSIDERING_COLOR = "blue"
    CONSIDERED_COLOR = "violet"
    PATH_COLOR = "yellow"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"


class node():
    def __init__(self, board, x, y, size):
        self.board = board
        self.col = x
        self.row = y
        self.size = size
        self.fill = False

        self.isStart = False
        self.isEnd = False
        self.considered = False
        self.considering = False
        self.obstacle = False
        self.path = False

        self.additionalProperties = {}

    def setPath(self):
        self.path = True

    def setObstacle(self):
        self.obstacle = not self.obstacle

    def setConsidering(self):
        self.considering = True

    def setConsidered(self):
        self.considered = True

    def markStart(self):
        self.isStart = True

    def isStartOrEnd(self):
        return self.isStart or self.isEnd

    def markEnd(self):
        self.isEnd = True

    def removeMarking(self):
        self.isStart = False
        self.isEnd = False
        self.fill = False

    def draw(self):
        fill = nodeColor.EMPTY_COLOR_BG
        if self.isStart:
            fill = nodeColor.START_COLOR
        elif self.isEnd:
            fill = nodeColor.END_COLOR
        elif self.path:
            fill = nodeColor.PATH_COLOR
        elif self.considering and not self.considered:
            fill = nodeColor.CONSIDERING_COLOR
        elif self.considered:
            fill = nodeColor.CONSIDERED_COLOR
        elif self.obstacle:
            fill = nodeColor.BLOCKED_COLOR

        outline = nodeColor.EMPTY_COLOR_BORDER

        xmin = self.col * self.size
        xmax = xmin + self.size
        ymin = self.row * self.size
        ymax = ymin + self.size
        self.board.create_rectangle(xmin, ymin, xmax, ymax, fill=fill, outline=outline)


class dijkstrasAlgorithm():
    weightStr = "Weight"
    ancestorStr = "Ancestor"
    timeSleep = 0.01

    def __init__(self, nodes, canvas):
        self.nodes = nodes
        self.canvas = canvas
        for i in self.nodes:
            for t in i:
                t.additionalProperties[self.weightStr] = 99999

    def createPath(self, end, start):
        curNode = end.additionalProperties[self.ancestorStr]
        while curNode != start:
            curNode.setPath()
            curNode.draw()
            self.canvas.update()
            curNode = curNode.additionalProperties[self.ancestorStr]

    def performAlgorithm(self):
        # Returns row, coloumn as [0] and [1]
        start = self.canvas.getStartCord()
        startNode = self.canvas.getNode(start[0], start[1])
        # Set start weight to 0
        startNode.additionalProperties[self.weightStr] = 0

        end = self.canvas.getEndCord()
        endNode = self.canvas.getNode(end[0], end[1])

        tQ = self.canvas.getAllNodes()
        Q = []
        for sublist in tQ:
            for item in sublist:
                Q.append(item)

        # Best Case
        adj = self.canvas.getAdjacent(start[0], start[1])
        if endNode in adj:
            print("Next to Me")
            return

        cur = start
        curNode = startNode
        while Q != []:
            for neighbours in self.canvas.getAdjacent(cur[0], cur[1]):
                if neighbours.additionalProperties[self.weightStr] > (curNode.additionalProperties[self.weightStr] + 1):
                    neighbours.additionalProperties[self.weightStr] = curNode.additionalProperties[self.weightStr] + 1
                    neighbours.additionalProperties[self.ancestorStr] = curNode
                    neighbours.setConsidering()
                    neighbours.draw()
                    self.canvas.update()
                    time.sleep(self.timeSleep)

            curNode.setConsidered()
            if curNode == endNode:
                print("Done")
                break
            curNode.draw()
            self.canvas.update()
            time.sleep(self.timeSleep)
            tempList = []
            for t in Q:
                if t.considered == False:
                    tempList.append(t)
            curNode = min(tempList, key=lambda x: x.additionalProperties[self.weightStr])
            cur = (curNode.row, curNode.col)

        self.createPath(endNode, startNode)


class nodeBoard(Canvas):
    def __init__(self, board, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, board, width=cellSize * columnNumber, height=(cellSize * (rowNumber + 0)), *args,
                        **kwargs)
        self.grid = [[node(self, x, y, cellSize) for x in range(columnNumber)] for y in range(rowNumber)]
        self.cellSize = cellSize
        self.columnNumber = columnNumber
        self.rowNumber = rowNumber
        self.currentDragged = []
        self.draw()
        self.bind("<Button-1>", self.click)
        self.bind('<Double-Button-1>', self.dblClick)
        self.bind("<Double-Button-3>", self.dblRightClick)

        self.bind("<B1-Motion>", self.drag)
        self.bind("<ButtonRelease-1>", self.release)
        self.start = None
        self.end = None

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def getAllNodes(self):
        return self.grid

    def getNode(self, row, col):
        return self.grid[row][col]

    def getStartCord(self):
        return self.start.row, self.start.col

    def getEndCord(self):
        return self.end.row, self.end.col

    def _exit(self):
        self.destroy()
        exit(0)

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def dblClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        if self.start is not None:
            self.start.removeMarking()
            self.start.draw()
        cell.markStart()
        cell.draw()
        self.start = cell

    def drawCell(self, cell):
        cell.draw()

    def dblRightClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        if self.end is not None:
            self.end.removeMarking()
            self.end.draw()
        cell.markEnd()
        cell.draw()
        self.end = cell
        algo = dijkstrasAlgorithm(self.grid, self)
        algo.performAlgorithm()

    def getAdjacent(self, row, col):
        adjList = []
        # print("row: %d, col: %d" %(col, row))
        if (col < self.columnNumber - 1):
            if self.grid[row][col + 1].obstacle == False:
                adjList.append(self.grid[row][col + 1])

        if (col - 1 >= 0):
            if self.grid[row][col - 1].obstacle == False:
                adjList.append(self.grid[row][col - 1])

        if (row < self.rowNumber - 1):
            if self.grid[row + 1][col].obstacle == False:
                adjList.append(self.grid[row + 1][col])

        if (row - 1 >= 0):
            if self.grid[row - 1][col].obstacle == False:
                adjList.append(self.grid[row - 1][col])
        return adjList

    def click(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        if not cell.isStartOrEnd():
            cell.setObstacle()
            self.currentDragged.append(cell)
        cell.draw()

    def drag(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        if cell not in self.currentDragged:
            cell.setObstacle()
            cell.draw()
            self.currentDragged.append(cell)

    def release(self, event):
        self.switched = []


if __name__ == "__main__":
    app = Tk()
    grid = nodeBoard(app, 25, 25, 25)
    grid.pack()
    app.mainloop()