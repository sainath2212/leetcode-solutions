class FooBar:
    def __init__(self, n):
        self.n = n
        self.foosem = threading.Semaphore(1)
        self.barsem = threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foosem.acquire()
            printFoo()
            self.barsem.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barsem.acquire()
            printBar()
            self.foosem.release()